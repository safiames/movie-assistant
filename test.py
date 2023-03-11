from datetime import datetime

now = datetime.now()

day = now.strftime("%A")
print("day:", day)