import ping3
import speedtest
import requests
import tkinter

WEBHOOK_URL = "https://discord.com/api/webhooks/1537425600757633034/i-RD_X_TlGEOy_dTjxh5Ghuhyf58U3teX600RqHeGQFeqkJQG4sF0H5Npfc527YkuSDE"

# Formatting pings:
user_id = "1436772413474869350"

data = {
    # Include ping syntax directly in the content string
    "content": f"Alert! <@{user_id}> check this out!"
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("Ping message sent successfully!")
else:
    print(f"Failed to send message: {response.status_code}")