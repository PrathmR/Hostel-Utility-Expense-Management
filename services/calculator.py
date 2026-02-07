TARIFF = {
    "electricity": 7.5,   # per unit
    "water": 2.0,         # per unit
    "wifi": 300           # fixed
}

def calculate_bill(electricity, water, wifi):
    return {
        "electricity_cost": electricity * TARIFF["electricity"],
        "water_cost": water * TARIFF["water"],
        "wifi_cost": TARIFF["wifi"],
        "total": (electricity * TARIFF["electricity"]) +
                 (water * TARIFF["water"]) +
                 TARIFF["wifi"]
    }
