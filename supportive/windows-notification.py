# pip install plyer

from plyer import notification
import time

# Send a toast notification
notification_title = "Notification Title"
notification_message = "This is a toast notification."
notification_timeout = 5  # Notification will disappear after 5 seconds

notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_timeout
)

# Sleep for a few seconds to keep the notification visible
time.sleep(notification_timeout)



