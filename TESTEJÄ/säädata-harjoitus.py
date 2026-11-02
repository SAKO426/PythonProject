
weather = [
    {"location": "Rovaniemi", "wind": 4.3}, # 0
    {"location": "oulu", "wind": 6.7},      # 1
    {"location": "Helsinki", "wind": 2.4},  # 2
    {"location": "espoo", "wind": 3.5},     # 3
    {"location": "jyväskylä", "wind": 3.2}, # 4
]

eniten_tuulee = weather[0]
vähiten_tuulee = weather[0]

for paikka in weather:
    if paikka["wind"] > eniten_tuulee["wind"]:
        eniten_tuulee = paikka

    if paikka["wind"] < vähiten_tuulee["wind"]:
        vähiten_tuulee = paikka


print(f"Eniten tuulee: {eniten_tuulee["location"]}, {eniten_tuulee ["wind"]}")
print(f"Vähiten tuulee: {vähiten_tuulee["location"]}, {vähiten_tuulee ["wind"]}")