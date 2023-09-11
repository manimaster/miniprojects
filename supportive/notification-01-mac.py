# The send_mac_notification function uses AppleScript to display a notification with the given title and message.
# In the if __name__ == "__main__": block, you can customize the notification_title and notification_message variables to send your desired notification.
# When you run this script, it will send a notification that appears in the macOS Notification Center, just like other applications' notifications.

import subprocess

def send_mac_notification(title, message):
    applescript_code = f'''
    display notification "{message}" with title "{title}"
    '''
    try:
        subprocess.run(['osascript', '-e', applescript_code])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    notification_title = "Notification Title"
    notification_message = "This is a macOS notification."

    send_mac_notification(notification_title, notification_message)
