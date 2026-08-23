import time
from ping3 import ping
import speedtest

TARGET_HOST = "1.1.1.1"

def check_ping():
    response_time = ping(TARGET_HOST, unit="ms")
    if response_time is None or response_time is False:
        return None
    return round(response_time, 2)

def run_speedtest():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    return round(download_speed, 2), round(upload_speed, 2)

def monitor():
    print("Starting network telemetry monitoring")
    latency = check_ping()

    if latency is None:
        print("Alert: Host is unreachable!")
        return

    print(f"Ping: {latency} ms")

    print("Running speed test (might take up to 20 seconds)")
    try:
        download, upload = run_speedtest()
        print(f"Download: {download} Mbps / Upload: {upload} Mbps")

    except Exception as e:
        print(f"Speed test failed: {e}")

if __name__ == "__main__":
    monitor()
