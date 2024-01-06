class Order:
    class Builder:
        def __init__(self):
            self.quantity = 0
            self.price = 0
            self.priceLimit = 0
            self.boughtOrSold = ""
            self.security = ""

        def buy(self, quantity, security):
            self.boughtOrSold = "Bought"
            self.quantity = quantity
            self.security = security
            return self

        def sell(self, quantity, security):
            self.boughtOrSold = "Sold"
            self.quantity = quantity
            self.security = security
            return self

        def atLimitPrice(self, p):
            self.priceLimit = p
            return self

        def build(self):
            return Order(self)

    def __init__(self, builder):
        self.quantity = builder.quantity
        self.price = builder.price
        self.priceLimit = builder.priceLimit
        self.boughtOrSold = builder.boughtOrSold
        self.security = builder.security



#order = Order.Builder().buy(100, "IBM").atLimitPrice(300).build()
order = (
    Order.Builder()
        .buy(100, "IBM")
        .atLimitPrice(300)
        .build()
)
print(order)