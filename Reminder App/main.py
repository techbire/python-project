
# make sure you entered this command in terminal before using [pip install plyer]
# you can also customize my project as per you need. For eg-you can modify as a daily word vocab reminder app



from plyer import notification
import time

def set_reminder(title, message, delay_seconds):
    notification.notify(
        title=title,
        message=message,
        app_name='Reminder App',
        timeout=10
    )
    time.sleep(delay_seconds)

if __name__ == "__main__":
    while True:
        title = input("Enter the reminder title: ")
        message = input("Enter the reminder message: ")
        delay_minutes = int(input("Enter the delay in minutes: "))

        delay_seconds = delay_minutes * 60

        set_reminder(title, message, delay_seconds)