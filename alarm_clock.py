import datetime
import time
import os


# Sends notification
def send_notification(title, message):
    applescript = """
    display notification "{}" with title "{}" sound name "Submarine"
    """.format(message, title)
    os.system("osascript -e '{}'".format(applescript))
    

alarm_time = input("Enter time for alarm (HH:MM) ").split(":")
title = input("Enter the title of your notification: ")
message = input("Enter the message of your notification: ")

while True:
    now = datetime.datetime.now()
    print(now)
    
    if int(alarm_time[0]) == now.hour and int(alarm_time[1]) == now.minute:
        send_notification(title, message)
        break
    else:
        time.sleep(1)
