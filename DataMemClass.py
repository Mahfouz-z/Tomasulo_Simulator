class dataMem:
    def __init__ (self, initDataPath):
        self.mem = [None] *  32000
        f=open(initDataPath, "r")
        dataEntries = f.readline()
        for line in dataEntries:
            addrValueArr = line.split(" ")
            self.mem[addrValueArr[0]] = addrValueArr[1]
        f.close()

    def update(self, wordAdd, data):
        self.mem[wordAdd] = data

    def getData(self, wordAdd):
        return self.mem[wordAdd]