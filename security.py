class Security:
    def __init__(self, security_name, security_type, price):
        self.security_name = security_name
        self.security_type = security_type
        self.price = price

    def printSecurity(self):
        print("Security:" + self.security_name + ", Type: " + self.security_type + ", Price: " + str(self.price))

