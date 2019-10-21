class priceStruct:
    def __init__(self, date, commodity, value):
        self.date = date
        self.commodity = commodity
        self.value = value
    
def readPricesDB(pricedbFile):
    file=open(pricedbFile, "r")
    content = ""
    listPrices = []
    for line in file:
        content = content + line
        splitArray = line.split(" ")
        #Check the first split
        if splitArray[0] == "N":
            commSymbol = splitArray[1]
            print("Commodity Symbol: " + splitArray[1])
        elif splitArray[0] == "P":
            slide = splitArray[4]
            slide = slide[2:]
            itemPriceStruct = priceStruct(splitArray[2],splitArray[3],slide)
            listPrices.append(itemPriceStruct)
    listPrices.insert(0,commSymbol)

    return listPrices