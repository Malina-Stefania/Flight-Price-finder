import requests
from bs4 import BeautifulSoup
from models import Flight
from utils import extract_all_prices


# extrage lista de orase (origin)
def get_available_origins():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.theflightdeal.com/flight-deals/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    origins = {}

    container = soup.find("div", class_="entry-content")

    links = container.find_all("a")

    for link in links:
        city = link.get_text().strip()
        href = link.get("href")

        if city and href:
            full_url = "https://www.theflightdeal.com" + href
            origins[city] = full_url

    return origins


# extrage zboruri pentru un oras
def scrape_city_flights(city_url):

    response = requests.get(city_url)
    soup = BeautifulSoup(response.text, "html.parser")

    flights = []

    deals = soup.find_all("article")

    for deal in deals:
        title_tag = deal.find("h2")

        if not title_tag:
            continue

        title = title_tag.get_text()

        prices = extract_all_prices(title)

        if not prices:
            continue

        origin = "Unknown"
        destination = "Unknown"

        if ":" in title:
            route_part = title.split(":")[1]

            if "–" in route_part:
                parts = route_part.split("–")

                if len(parts) >= 2:
                    origin = parts[0].strip()
                    destination = parts[1].split("$")[0].strip()

        flight = Flight(
            origin=origin,
            destination=destination,
            prices=prices,
            source="TheFlightDeal"
        )

        flights.append(flight)

    return flights