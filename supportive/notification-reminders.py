# This Python script uses AppleScript to extract recent notifications from macOS and adds them to the Reminders app. Here's how it works:

# get_notifications function uses AppleScript to retrieve recent notifications from all running processes.

# add_to_reminders function takes the notifications and uses AppleScript to create new reminders in the Reminders app.

# In the if __name__ == "__main__": block, we retrieve notifications and then add them to the Reminders app.

# Manikandan (c) 2018

import subprocess

def get_notifications():
    # Use AppleScript to get recent notifications
    applescript_code = """
    set notificationList to {}
    tell application "System Events"
        set allProcesses to application processes
        repeat with proc in allProcesses
            tell proc
                try
                    set processName to name
                    set processID to id
                    set notificationCenter to get every notification of application processName
                    repeat with notify in notificationCenter
                        set appName to displayed name of notify
                        set notifyTitle to title of notify
                        set notifySubtitle to subtitle of notify
                        set notifyBody to text of notify
                        set notificationList to notificationList & {{"app": appName, "title": notifyTitle, "subtitle": notifySubtitle, "body": notifyBody}}
                    end repeat
                end try
            end tell
        end repeat
    end tell
    return notificationList
    """
    
    try:
        result = subprocess.run(['osascript', '-e', applescript_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return eval(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def add_to_reminders(notifications):
    # Use AppleScript to add notifications to Reminders app
    for notification in notifications:
        title = notification["title"]
        subtitle = notification["subtitle"]
        body = notification["body"]
        applescript_code = f"""
        tell application "Reminders"
            set newReminder to make new reminder
            set name of newReminder to "{title}"
            set body of newReminder to "{body}"
        end tell
        """
        try:
            subprocess.run(['osascript', '-e', applescript_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Added to Reminders: {title}")
        except Exception as e:
            print(f"An error occurred while adding to Reminders: {e}")

if __name__ == "__main__":
    notifications = get_notifications()
    if notifications:
        add_to_reminders(notifications)
