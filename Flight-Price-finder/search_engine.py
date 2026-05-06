
class SearchEngine:

    def search_by_destination(self, flights, destination):
        results = []

        for flight in flights:
            if destination.lower() in flight.destination.lower():
                results.append(flight)

        return results