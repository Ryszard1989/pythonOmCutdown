from security import Security

class Position:
    def __init__(self, security, amount):
        self.security = security
        self.amount = amount

class Portfolio:
    def __init__(self, portfolioManager):
        self.positions = []
        self.portfolioManager = portfolioManager
            
    def calculateNewPositionAveragePrice(self, positionSecurity, positionAmount, tradeSecurity, tradeAmount):
        totalAmount = positionAmount + tradeAmount
        positionWeight = positionSecurity.price * positionAmount
        tradeWeight = tradeSecurity.price * tradeAmount
        weightedAverage = (positionWeight + tradeWeight) / totalAmount
        return weightedAverage
        

    def makeTrade(self, security, amount):
        print("Trading " + str(amount) + " of " + security.securityName + " at price of " + str(security.price))
        foundFlag = False
        if self.positions:
            for p in self.positions:
                if p.security.securityName == security.securityName:
                    foundFlag = True
                    newAveragePrice = self.calculateNewPositionAveragePrice(p.security, p.amount, security, amount)
                    #print("New average px of " + p.security.securityName + ":" + str(newAveragePrice))
                    p.amount += amount
                    p.security.price = newAveragePrice
        if foundFlag == False:
            newSecurity = Security(security.securityName, security.securityType, security.price)
            self.positions.append(Position(newSecurity, amount))



    def printPortfolio(self):
        print(self.portfolioManager + "'s Portfolio:")
        for p in self.positions:
            print("Security: " + p.security.securityName + ", Amount: " + str(p.amount) + ", AveragePrice: " + str(p.security.price))


