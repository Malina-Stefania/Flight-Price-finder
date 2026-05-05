class Flight:
    def __init__(self, origin, destination, prices, source):

        self.origin = origin
        self.destination = destination
        self.prices = prices
        self.source = source

    def __str__(self):
        prices_str = ""

        for category, price in self.prices.items():
            prices_str += category + ": " + str(price) + "$, "

        prices_str = prices_str.rstrip(", ")

        return self.origin + " -> " + self.destination + " | " + prices_str + " | " + self.source