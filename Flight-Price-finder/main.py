from scraper import get_available_origins, scrape_city_flights
from search_engine import SearchEngine
from utils import get_similar_destinations


def main():
    print("=== Flight Finder ===")

    origin_input = input("Enter origin: ")
    destination = input("Enter destination: ")

    print("\nLoading available origins...\n")

    origins = get_available_origins()

    if origin_input not in origins:
        print("Origin not found on site.")
        return

    city_url = origins[origin_input]

    print("Searching flights...\n")

    flights = scrape_city_flights(city_url)

    engine = SearchEngine()

    results = engine.search_by_destination(flights, destination)

    if results:
        print("Results found:\n")

        results = sorted(results, key=lambda x: min(x.prices.values()))

        for flight in results[:5]:
            print(flight)

    else:
        print("No results found for your destination.\n")
        print("Trying similar destinations...\n")

        similar = get_similar_destinations(destination)

        found = False

        for dest in similar:
            results = engine.search_by_destination(flights, dest)

            if results:
                print("Found results for:", dest, "\n")

                results = sorted(results, key=lambda x: min(x.prices.values()))

                for flight in results[:5]:
                    print(flight)

                found = True
                break

        if not found:
            print("No flights found at all.")

if __name__ == "__main__":
    main()