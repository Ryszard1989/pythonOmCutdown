from portfolio import Portfolio
from stockExchange import StockExchange
from security import Security

class InteractiveSession:
    def __init__ (self, stockExchange):
        self.stockExchange = stockExchange
        userName = input("Hi trader, what's your name?\n")
        self.portfolio = Portfolio(userName)

        print("Play till 5 days have passed see if your portfolio prices are better than the market's!\n")
        print("Trading has begun!")

    def session(self):
        self.stockExchange.printStockExchange()
        validMenuOptions = ['T','t','V','v','P','p','Q','q']
        dayCount = 1
        while(dayCount <= 5):
            print("------------------------------------------------------")
            print("'T' - Trade")
            print("'V' - View Market")
            print("'P' - View Portfolio")
            print("'Q' - Quit/End Simulation")
            menuOption = input("Select an option from the above\n")
            print("------------------------------------------------------")
            if menuOption not in validMenuOptions:
                print ("invalid menu option\n")
            else:
                # Trade
                if menuOption in ['T','t']:
                    print("Time to make today's trades.")
                    self.stockExchange.printStockExchange()
                    securitySelection = int(input("Choose the number of the stock you want to trade\n"))
                    if(securitySelection > len(self.stockExchange.securities)):
                        print("Sorry, that's not a valid stock\n")
                    else:
                        securityAmount = int(input("How much do you want to buy/sell? (use minus sign to sell)\n"))
                        self.portfolio.makeTrade(self.stockExchange.securities[securitySelection-1], securityAmount)
                    userinput = input("Are you done trading for today? (Choose y/n)\n")
                    if userinput in ['Y','y','N','n']:
                        if userinput in ['Y','y']:
                            print("Ok that's it for today. Let's see how that goes tomorrow\n")                            
                            dayCount += 1
                            self.stockExchange.simulateDay()
                            
                        elif userinput in ['N','n']:
                            print("Back to the menu then\n")
                    else:
                        print("Hmmm, that wasn't a yes or a no. We'll assume you're done. Let's see how that goes tomorrow\n")                            
                        self.stockExchange.simulateDay()

                # View Market
                elif menuOption in ['V','v']:
                    print("View today's market")
                    self.stockExchange.printStockExchange()
                # View Portfolio
                elif menuOption in ['P','p']:

                    print("View portfolio for Day " + str(self.stockExchange.day))
                    self.portfolio.printPortfolio()
                # Quit
                elif menuOption in ['Q','q']:
                    break
            
        print("Your final portfolio:")
        self.portfolio.printPortfolio()
        print("\nThanks for playing!\n")