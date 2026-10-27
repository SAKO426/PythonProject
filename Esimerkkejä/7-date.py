# pelkkä päivämäärä

from datetime import date

today = date.today()
print("Tänään on", today)

# päivämäärä + aika
from datetime import datetime

today = datetime.now()
date_text = today.strftime("%d/%m/%Y %H:%M:%S")
print(f"Päivämäärä: {date_text}")

# Kuinka monta päivämäärää on kahden
# Päivämäärän välillä?
import datetime
first = date(2020, 9, 4)
second = date(2020, 11, 20)
delta = second - first
days = delta.days
print(f"Päiviä: {days}")

from datetime import datetime
from datetime import timedelta
#mikä päivä on jos tähän päivään lisätään 45 päivää?

today = datetime.now()
today = today + timedelta(45)
print(f"Päiväsi 45:n päivän päästä on: {today}")