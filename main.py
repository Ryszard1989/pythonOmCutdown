#TODO - Move all this to a test file.
#TODO - Read positions from file on start.
#TODO - Write positions to file on start.

from security import Security
from stockExchange import StockExchange
from portfolio import *

ftse = StockExchange("FTSE 100")
securities = [Security("IBM","Equity",105), Security("VOD","Equity",108), Security("UBI","Equity",120)]
ftse.addSecurities(securities)

myPortfolio = Portfolio()

ftse.calculateAveragePrice()
ftse.printStockExchange()

print("Day 0 Trading Action")

myPortfolio.makeTrade(ftse.securities[0], 100)
myPortfolio.makeTrade(ftse.securities[2], 500)
print("Portfolio end of day")
myPortfolio.printPortfolio()


ftse.simulateDay()

print("Day 1 Trading Action")
myPortfolio.makeTrade(ftse.securities[0], 100)
myPortfolio.makeTrade(ftse.securities[1], 100)
myPortfolio.printPortfolio()


