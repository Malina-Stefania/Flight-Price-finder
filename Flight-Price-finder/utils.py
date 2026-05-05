import re
from datetime import datetime, timedelta


def extract_all_prices(text):
    prices = {}

    parts = text.split("/")

    for part in parts:
        part = part.strip()

        if "$" in part:
            try:
                price_part = part.split("$")[1]
                price = int(price_part.split()[0])

                if "(" in part and ")" in part:
                    category = part.split("(")[1].split(")")[0]
                else:
                    category = "Standard"

                prices[category.strip()] = price

            except:
                continue

    return prices


def get_similar_destinations(destination):
    similar = {
        "Paris": ["Brussels", "Amsterdam"],
        "Rome": ["Milan", "Naples"],
        "London": ["Manchester", "Dublin"],
        "Barcelona": ["Madrid", "Valencia"],
        "New York": ["Boston", "Philadelphia", "Washington D.C."],
        "Los Angeles": ["San Diego", "San Francisco", "Las Vegas"],
        "Miami": ["Orlando", "Tampa", "Cancun"],
        "São Paulo": ["Rio de Janeiro", "Buenos Aires", "Santiago"],
        "Tokyo": ["Osaka", "Seoul", "Kyoto"],
        "Bangkok": ["Phuket", "Kuala Lumpur", "Singapore"],
        "Dubai": ["Doha", "Abu Dhabi", "Muscat"],
        "Delhi": ["Mumbai", "Jaipur", "Bangalore"],
        "Beijing": ["Shanghai", "Hong Kong", "Seoul"]
    }

    if destination in similar:
        return similar[destination]

    return []