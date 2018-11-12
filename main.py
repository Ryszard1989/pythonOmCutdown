#TODO - Move all this to a test file.
#TODO - Read positions from file on start.
#TODO - Write positions to file on start.

from security import Security
from stockExchange import StockExchange
from portfolio import Position
from portfolio import Portfolio
from interactiveSession import InteractiveSession

ftse = StockExchange("FTSE 100")
securities = [Security("IBM","Equity",105), Security("VOD","Equity",108), Security("UBI","Equity",120)]
ftse.addSecurities(securities)

uiSession = InteractiveSession(ftse)
uiSession.session()

