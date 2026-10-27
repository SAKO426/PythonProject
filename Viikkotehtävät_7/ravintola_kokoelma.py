
# Lista ravintoloista
restaurants = [
    {
        "name": "North Delish",
        "rating": 4.5,
        "reservations": True,
        "services": ["lunch", "dinner"],
        "price_level": 5,
        "location": "Rovaniemi"
    },
    {
        "name": "Food Galore",
        "rating": 3.8,
        "reservations": False,
        "services": ["breakfast", "lunch"],
        "price_level": 3,
        "location": "Tornio"
    },
    {
        "name": "Snacksy Oy",
        "rating": 3.2,
        "reservations": False,
        "services": ["lunch", "dinner", "night"],
        "price_level": 2,
        "location": "Oulu"
    },
    {
        "name": "Pizza House",
        "rating": 4.7,
        "reservations": True,
        "services": ["lunch", "dinner"],
        "price_level": 4,
        "location": "Kajaani"
    },
    {"name": "Rats On A Stick",
     "rating": 4.9,
     "reservations": True,
     "services": ["lunch", "dinner", "night"],
     "price_level": 5,
     "location": " Kauhajoen jätevedenpuhdistamo"
    }
]

# Käyttäjän syötteet
min_rating = float(input("Monenko tähden ravintolan haluat vähintään? (1-5)"))

max_price = float(input("Kuinka persaukinen olet? (Anna ravintolan hinta-taso 1-5)"))

reservation = input("Haluatko tehdä etukäteen varauksen? (k/e)")

hour = int(input("Mihin kelloaikaan halauat ruokailla (0-23)"))


# aamupalan ajat
if 6 <= hour <= 10:
    wanted_service = "breakfast"

#lounas
elif 11 <= hour <= 16:
    wanted_service = "lunch"

elif 17 <= hour <= 19:
    wanted_service = "dinner"

else:
    wanted_service = "night"


found = False

for restaurant in restaurants:

    if restaurant["rating"] < min_rating:
        continue

    if restaurant["price_level"] > max_price:
        continue

    if wanted_service not in restaurant["services"]:
        continue

    if reservation == "k" and restaurant["reservations"] == False:
        continue

    print(restaurant["name"])
    found = True

if not found:
    print("Valitettavasti sopivaa ravintolaa ei löytynyt!")