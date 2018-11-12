from security import Security

class Position:
    def __init__(self, security, amount):
        self.security = security
        self.amount = amount

class Portfolio:
    def __init__(self, portfolioManager):
        self.positions = []
        self.portfolioManager = portfolioManager
        self.cash = 10000 #TODO pass in value
        self.portfolioValue = 0 # Value of stocks in portfolio
        self.totalValue = 10000 # Total value of stocks + cash
            
    def calculateNewPositionAveragePrice(self, positionSecurity, positionAmount, tradeSecurity, tradeAmount):
        totalAmount = positionAmount + tradeAmount
        if totalAmount is 0:
            return 0
        positionWeight = positionSecurity.price * positionAmount
        tradeWeight = tradeSecurity.price * tradeAmount
        weightedAverage = (positionWeight + tradeWeight) / totalAmount
        return weightedAverage

    #TODO - Look at changing this to just calculate delta rather than full recalc
    def calculatePortfolioValue(self):
        newPortfolioValue = 0
        for p in self.positions:
            newPortfolioValue += (p.security.price * p.amount)
        self.portfolioValue = newPortfolioValue

    #TODO - Look at changing this to just calculate delta rather than full recalc
    def calculateTotalValue(self):
        self.calculatePortfolioValue() #Make sure portfolio value always up to date. Look at killing unnescary recalc later.
        self.totalValue = self.portfolioValue + self.cash

    def makeTrade(self, security, amount):
        if amount is 0:
            print("Entered trading amount of 0")
            return
        print("Trading " + str(amount) + " of " + security.securityName + " at price of " + str(security.price))
        foundFlag = False
        if self.positions:
            for p in self.positions:
                if p.security.securityName == security.securityName:
                    foundFlag = True
                    newAveragePrice = self.calculateNewPositionAveragePrice(p.security, p.amount, security, amount)
                    p.amount += amount
                    p.security.price = newAveragePrice
                    if p.amount is 0:
                        self.positions.remove(p)
        if foundFlag == False:
            newSecurity = Security(security.securityName, security.securityType, security.price)
            self.positions.append(Position(newSecurity, amount))
        self.cash -= (security.price * amount)
        self.calculatePortfolioValue()
        self.calculateTotalValue()


    def printPortfolio(self):
        print(self.portfolioManager + "'s Portfolio:")
        print("Total Value: " + str(self.totalValue))
        print("Value of stocks in portfolio: " + str(self.portfolioValue))
        print("Available cash: " + str(self.cash))
        for p in self.positions:
            print("Security: " + p.security.securityName + ", Amount: " + str(p.amount) + ", AveragePrice: " + str(p.security.price))