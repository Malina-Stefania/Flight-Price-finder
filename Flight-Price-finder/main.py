from scraper import get_available_origins, scrape_city_flights
from search_engine import SearchEngine
from utils import get_similar_destinations, get_similar_origins


def main():
    print("=== Flight Finder ===")

    while True:
        origin_input = input("\nEnter origin: ")
        destination = input("Enter destination: ")

        origins = get_available_origins()
        engine = SearchEngine()

        flights = []
        used_similar_origin = None

        if origin_input in origins:
            print("Searching flights...\n")
            flights = scrape_city_flights(origins[origin_input])

        else:
            print("\nOrigin not found. Trying similar origins...\n")
            similar_origins = get_similar_origins(origin_input)

            for sim_origin in similar_origins:
                if sim_origin in origins:
                    print("Trying:", sim_origin)

                    flights = scrape_city_flights(origins[sim_origin])

                    if flights:
                        used_similar_origin = sim_origin
                        break

            if not flights:
                print("No flights found from similar origins.")

                again = input("\nSearch again? (yes/no): ")
                if again.lower() != "yes":
                    print("Goodbye!")
                    break
                else:
                    continue

        results = engine.search_by_destination(flights, destination)

        if results:
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

        again = input("\nSearch another flight? (yes/no): ")

        if again.lower() != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()