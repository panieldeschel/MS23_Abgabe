class SchalterPermanent:
    def __init__(self, address, id):
        self.address = address
        self.id = id
        self.power_status = None
        self.max_watt = None
        self.cooldown = None

    def __sendToIP(self, text):
        #send via TCP
        return

    def printMe(self):
        print(f"ID{self.id} of {self.address}")
        return self

    def setPower(self, power_status):
        if self.power_status:
            self.__sendToIP(f"{self.id} turn on")
        else:
            self.__sendToIP(f"{self.id} turn off")
        self.power_status = power_status
        print(f"Set Power to {power_status}")
        return self
    
    def setMax(self, max_watt):
        self.__sendToIP(f"{self.id} max_watt {self.max_watt}")
        self.max_watt = max_watt
        print(f"Set max Wattage to {max_watt}W")
        return self
    
    def setCooldown(self, cooldown):
        self.__sendToIP(f"{self.id} cooldown {self.cooldown}")
        self.cooldown = cooldown
        print(f"Set Cooldown to {cooldown}min")
        return self

# with Expression Builder
class SchalterBuilder:
    class Builder:
        def __init__(self, address, id):
            self.address = address
            self.id = id
            self.power_status = None
            self.max_watt = None
            self.cooldown = None

        def power(self, power_status):
            self.power_status = power_status
            return self

        def setMax(self, max_watt):
            self.max_watt = max_watt
            return self

        def setCooldown(self, cooldown):
            self.cooldown = cooldown
            return self

        def build(self):
            return SchalterBuilder(self)

    def __init__(self, builder):
        self.address = builder.address
        self.id = builder.id
        self.power_status = builder.power_status
        self.max_watt = builder.max_watt
        self.cooldown = builder.cooldown
    
    def send(self):
        # Hier wenn power, max_watt und cooldown
        # als einzelne Commands wie in SchalterPermanent senden,
        # wenn sie != None
        print(f"Sending Commands to ID{self.id} of {self.address}:\nPower: {self.power_status}\nMax_Watt: {self.max_watt}W\nCooldown: {self.cooldown}min")
        return



windrad1 = (
    SchalterPermanent("123.456.789", 1)
        .printMe()
        .setPower(True)
        .setCooldown(15)
        .setMax(300)
)

print(f"\n")

windrad2 = (
    SchalterBuilder.Builder("123.456.789", 2)
        .power(True)
        .setCooldown(10)
        .setMax(300)   
        .build()    
    .send()
)

print(f"\n")

(
    windrad1
        .printMe()
        .setPower(False)
)
