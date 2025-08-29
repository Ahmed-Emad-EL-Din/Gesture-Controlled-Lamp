import websocket

# ESP8266 WebSocket URL (replace with your ESP8266 IP address)
ESP_URL = "ws://192.168.1.10/ws"   

def send_command(command):
    try:
        # Connect to ESP8266 WebSocket
        ws = websocket.WebSocket()
        ws.connect(ESP_URL)

        # Send the command (string)
        ws.send(command)
        print(f"Sent: {command}")

        # (Optional) Wait for response
        response = ws.recv()
        print(f"Received from ESP: {response}")

        # Close connection
        ws.close()
    except Exception as e:
        print(f"Error: {e}")

'''
# Example usage:
send_command("on")
send_command("off")
send_command("toggle")
'''

def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        send_command("off")
    elif fingerUp==[0,1,0,0,0]:
        send_command("on")
