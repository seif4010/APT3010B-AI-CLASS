# candy store that has 8 candies
# when it reaches 50% it should tell the store owner to fill them
# using Object oriented within it
import random


class Candies(object):
    def __init__(self):
        self.Candies = ["Choco": "Pentos": "Tropicals": "PK's": "Fanta": "Ngumu": "Cola": "BIGGIE G"]
        self.CandiesLocation = {"Choco": '0', "Pentos": '0', "Tropicals": '0',
                                "PK": '0', "Fanta": '0', "Ngumu": '0', "Cola": '0', "BIGGIE G": '0'}

        # random
        self.CandiesLocation["Choco"] = random.randint(0, 1)
        self.CandiesLocation["Pentos"] = random.randint(0, 1)
        self.CandiesLocation["Tropicals"] = random.randint(0, 1)
        self.CandiesLocation["PK's"] = random.randint(0, 1)
        self.CandiesLocation["Fanta"] = random.randint(0, 1)
        self.CandiesLocation["Ngumu"] = random.randint(0, 1)
        self.CandiesLocation["Cola"] = random.randint(0, 1)
        self.CandiesLocation["BIGGIE G"] = random.randint(0, 1)

        # placing it on random locations
        self.checkCandies = random.choice(self.Candies)


class Reflexstore(Candies):
    def __init__(self, Candies):
        # random condions
        print(Candies.CandiesLocation)
        print("Monitor them all randomly", Candies.checkCandies)
        # when it's almost empty
        count = 0
        n = 0

        while count > 8:
            if Candies.CandiesLocation(Candies.checkCandies) < 50:
                Candies.CandiesLocation(Candies.checkCandies) = 100
                print(Candies.checkCandies, "They have been refilled")
            else:
                print(Candies.checkCandies, "They have not reached below 50")
