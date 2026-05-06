import re
from datetime import datetime, timedelta

similar = {
        "New York": ["New York City", "Philadelphia", "Boston", "Washington D.C."],
        "Newark": ["New York City", "Philadelphia"],
        "Jersey City": ["New York City", "Philadelphia"],
        "Baltimore": ["Washington D.C.", "Philadelphia"],
        "Boston": ["Boston", "New York City"],
        "Providence": ["Boston", "New York City"],
        "Detroit": ["Chicago"],
        "Cleveland": ["Chicago"],
        "Columbus": ["Chicago"],
        "Indianapolis": ["Chicago"],
        "Milwaukee": ["Chicago"],
        "St. Louis": ["Chicago", "Dallas"],
        "Houston": ["Dallas"],
        "Austin": ["Dallas"],
        "San Antonio": ["Dallas"],
        "Orlando": ["Miami"],
        "Tampa": ["Miami"],
        "Atlanta": ["Miami", "Dallas"],
        "Charlotte": ["Washington D.C.", "Miami"],
        "Nashville": ["Dallas", "Chicago"],
        "San Jose": ["San Francisco"],
        "Oakland": ["San Francisco"],
        "Sacramento": ["San Francisco"],
        "San Diego": ["Los Angeles"],
        "Las Vegas": ["Los Angeles", "Phoenix"],
        "Fresno": ["Los Angeles", "San Francisco"],
        "Spokane": ["Seattle", "Portland"],
        "Boise": ["Seattle", "Portland"],
        "Eugene": ["Portland"],
        "Salem": ["Portland"],
        "Tucson": ["Phoenix"],
        "Albuquerque": ["Phoenix", "Dallas"],
        "El Paso": ["Dallas", "Phoenix"],
        "California": ["Los Angeles", "San Francisco"],
        "Texas": ["Dallas"],
        "Florida": ["Miami"],
        "Washington": ["Seattle"],
        "Oregon": ["Portland"]
    }

def get_similar_cities(city):
    city = city.title()

    if city in similar:
        return similar[city]

    return []

def get_similar_origins(origin):
    return get_similar_cities(origin)


def get_similar_destinations(destination):
    return get_similar_cities(destination)

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