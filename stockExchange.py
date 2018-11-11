from security import Security
import random

class StockExchange:
    def __init__(self, name):
        self.name = name
        self.securities = []
        self.averagePrice = 0
        self.day = 1

    def addSecurity(self, security):
        self.securities.append(security)

    def calculateAveragePrice(self):
        total = 0
        for s in self.securities:
            total+= s.price
        self.averagePrice = total / self.securities.__len__()

    def addSecurities(self, securities):
        for s in securities:
            self.addSecurity(s)
        self.calculateAveragePrice

    def simulateDay(self):
        print()
        for s in self.securities:
            s.price += random.randint(-10,10)
            if s.price < 0:
                s.price = 0
        self.calculateAveragePrice()
        self.day += 1
        self.printStockExchange()

    def printStockExchange(self):
        print("Day " + str(self.day))
        print("Stock Exchange: " + self.name)
        print("Average Price of Stocks: " + str(self.averagePrice))
        count = 1
        for s in self.securities:
            print(str(count) + ": " + s.stringSecurity())
            count += 1
        print("")