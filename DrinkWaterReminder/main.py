import time
from plyer import notification

while True:
    print("Drink some water")
    notification.notify(title = "You need to drink some water", message = "Drink water")
    time.sleep(60*60)