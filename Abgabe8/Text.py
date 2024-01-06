class Text:
    def __init__(self, text):
        self.myText = text
        self.myColor = "white"
        self.mySize = 10
        self.myFont = "Arial"

    def color(self, c):
        self.myColor = c
        return self

    def size(self, s):
        self.mySize = s
        return self

    def font(self, f):
        self.myFont = f
        return self

    def __str__(self):
        return f"Text: {self.myText}\nFarbe: {self.myColor}\nGröße: {self.mySize}px\nSchriftart: {self.myFont}"

#text = Text("Test").color("blau").size(12).font("Calibri")
text = (
    Text("Test")
        .color("blau")
        .size(12)
        .font("Calibri")
)
print(text)