class dataMem:
    def __init__ (self, initDataPath):
        self.mem = [None] *  32000
        f=open(initDataPath, "r")
        dataEntries = f.read()
        f.close()
        dataEntries=dataEntries.split('\n')
        for line in dataEntries:
            addrValueArr = line.split(" ")
            self.mem[int(addrValueArr[0])] = int(addrValueArr[1])

    def update(self, wordAdd, data):
        self.mem[wordAdd] = data

    def getData(self, wordAdd):
        return self.mem[wordAdd]