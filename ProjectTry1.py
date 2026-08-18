import time
import requests
from ping3 import ping
import speedtest

# --- CONFIGURATION ---
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1537425600757633034/i-RD_X_TlGEOy_dTjxh5Ghuhyf58U3teX600RqHeGQFeqkJQG4sF0H5Npfc527YkuSDE"
MAX_LATENCY_MS = 120  # Alert if ping exceeds 100ms
MIN_DOWNLOAD_MBPS = 25.0  # Alert if download drops below 25 Mbps
TARGET_HOST = "1.1.1.1"  # Cloudflare DNS for quick ping checks


def send_discord_alert(title, description, color=15158332):
    """Sends a formatted embed notification to Discord."""
    payload = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color  # Red = 15158332, Orange = 15105570
            }
        ]
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Failed to send alert: {e}")


def check_ping():
    """Checks latency to the target host."""
    response_time = ping(TARGET_HOST, unit='ms')
    if response_time is None or response_time is False:
        return None  # Host unreachable / Packet loss
    return round(response_time, 2)


def run_speedtest():
    """Runs bandwidth test for download/upload in Mbps."""
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert bits to Megabits
    upload_speed = st.upload() / 1_000_000
    return round(download_speed, 2), round(upload_speed, 2)


def monitor():
    print("Starting network telemetry monitoring...")

    # 1. Quick Latency Check
    latency = check_ping()

    if latency is None:
        print("ALERT: Host unreachable!")
        send_discord_alert("🚨 NETWORK DOWN", f"Target host `{TARGET_HOST}` is unreachable. Total packet loss.")
        return

    print(f"Ping: {latency} ms")
    if latency > MAX_LATENCY_MS:
        send_discord_alert("⚠️ HIGH LATENCY DETECTED",
                           f"Current ping to `{TARGET_HOST}` is **{latency} ms** (Threshold: {MAX_LATENCY_MS} ms).")

    # 2. Bandwidth Test
    print("Running speed test (this takes ~20 seconds)...")
    try:
        download, upload = run_speedtest()
        print(f"Download: {download} Mbps | Upload: {upload} Mbps")

        if download < MIN_DOWNLOAD_MBPS:
            send_discord_alert(
                "📉 BANDWIDTH DEGRADATION",
                f"Download speed dropped to **{download} Mbps** (Minimum expected: {MIN_DOWNLOAD_MBPS} Mbps).\nUpload: {upload} Mbps."
            )
    except Exception as e:
        print(f"Speed test failed: {e}")


if __name__ == "__main__":
    monitor()