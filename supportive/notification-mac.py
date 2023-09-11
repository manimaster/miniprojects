import subprocess

def send_mac_alert(title, message):
    applescript_code = f'''
    display alert "{title}" message "{message}" as critical
    '''
    try:
        subprocess.run(['osascript', '-e', applescript_code])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    alert_title = "Alert Title"
    alert_message = "This is a macOS alert notification."

    send_mac_alert(alert_title, alert_message)
