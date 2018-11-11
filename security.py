class Security:
    def __init__(self, securityName, securityType, price):
        self.securityName = securityName
        self.securityType = securityType
        self.price = price

    def printSecurity(self):
        print("Security:" + self.securityName + ", Type: " + self.securityType + ", Price: " + str(self.price))

