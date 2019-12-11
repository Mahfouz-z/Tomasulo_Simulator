class RS:
    def __init__(self, station_num):
        self.station_num = station_num #TODO take it from a file
        self.index = {}
        self.index["lw"] = 0
        self.index["sw"] = self.index["lw"] + self.station_num["lw"]
        self.index["jmp"] = self.index["sw"] + self.station_num["sw"]
        self.index["jalr"] = self.index["sw"] + self.station_num["sw"]
        self.index["ret"] = self.index["sw"] + self.station_num["sw"]
        self.index["beq"] = self.index["jmp"] + self.station_num["jmp"]
        self.index["add"] = self.index["beq"] + self.station_num["beq"]
        self.index["sub"] = self.index["beq"] + self.station_num["beq"]
        self.index["addi"] = self.index["beq"] + self.station_num["beq"]
        self.index["nand"] = self.index["add"] + self.station_num["add"]
        self.index["mult"] = self.index["nand"] + self.station_num["nand"]

        self.used = {}
        self.used["lw"] = 0
        self.used["sw"] = 0
        self.used["jmp"] = 0
        self.used["beq"] = 0
        self.used["add"] = 0
        self.used["nand"] = 0
        self.used["mult"] = 0

        self.station = []

        for i in range(self.station_num["lw"]):
            station_entry = {}
            station_entry["name"] = "lw" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

        for i in range(self.station_num["sw"]):
            station_entry = {}
            station_entry["name"] = "sw" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

        for i in range(self.station_num["jmp"]):
            station_entry = {}
            station_entry["name"] = "jmp" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

        for i in range(self.station_num["beq"]):
            station_entry = {}
            station_entry["name"] = "beq" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

        for i in range(self.station_num["add"]):
            station_entry = {}
            station_entry["name"] = "add" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

        for i in range(self.station_num["nand"]):
            station_entry = {}
            station_entry["name"] = "nand" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

        for i in range(self.station_num["mult"]):
            station_entry = {}
            station_entry["name"] = "mult" + str(i)
            station_entry["busy"] = False
            station_entry["op"] = "init"
            station_entry["Vj"] = 0
            station_entry["Vk"] = 0
            station_entry["Qj"] = "init"
            station_entry["Qk"] = "init"
            station_entry["dest"] = 0
            station_entry["A"] = 0
            station_entry["status"] = "init"
            self.station.append(station_entry)

    def update_station(self, name, index, busy, op, Vj, Vk, Qj, Qk, dest, A, status):
        self.station[self.index[name] + index]["busy"] = busy
        self.station[self.index[name] + index]["op"] = op
        self.station[self.index[name] + index]["Vj"] = Vj
        self.station[self.index[name] + index]["Vk"] = Vk
        self.station[self.index[name] + index]["Qj"] = Qj
        self.station[self.index[name] + index]["Qk"] = Qk
        self.station[self.index[name] + index]["dest"] = dest
        self.station[self.index[name] + index]["A"] = A
        self.station[self.index[name] + index]["status"] = status

    def issue(self, name, Vj, Vk, Qj, Qk, dest, A):
        index = self.used["add"] if (name == "add" or name == "sub" or name == "addi") else self.used["jmp"] if (name == "jmp" or name == "jalr" or name == "ret") else self.used[name]
        self.station[self.index[name] + index]["busy"] = True
        self.station[self.index[name] + index]["op"] = name
        self.station[self.index[name] + index]["Vj"] = Vj if (Qj == None) else 0
        self.station[self.index[name] + index]["Vk"] = Vk if (Qk == None) else 0
        self.station[self.index[name] + index]["Qj"] = 0 if (Qj == None) else Qj
        self.station[self.index[name] + index]["Qk"] = 0 if (Qk == None) else Qk
        self.station[self.index[name] + index]["dest"] = dest
        self.station[self.index[name] + index]["A"] = A
        self.station[self.index[name] + index]["status"] = "issued"

        if (name == "add" or name == "sub" or name == "addi"):
            self.used["add"] += 1
        elif (name == "jmp" or name == "jalr" or name == "ret"):
            self.used["jmp"] += 1
        else:
            self.used[name] += 1

    def available(self, name):
        if (name == "add" or name == "sub" or name == "addi"):
            return self.used["add"] < self.station_num["add"]
        elif (name == "jmp" or name == "jalr" or name == "ret"):
            return self.used["jmp"] < self.station_num["jmp"]
        else:
            return self.used[name] < self.station_num[name]

    def ready(self, index):
        return ((self.station[index]["Qj"] == 0) and (self.station[index]["Qj"] == 0) and (self.station[index]["status"] == "issued"))

    def station_num_total(self):
        return self.index["mult"] + self.station_num["mult"]

    def execute(self, index):
        self.station[index]["status"] = "executed"
        return self.station[index]["op"], self.station[index]["Qj"], self.station[index]["Qk"], self.station[index]["A"], index

    def write(self, index):
        self.station[index]["busy"] = False
        self.station[index]["op"] = "init"
        self.station[index]["Vj"] = 0
        self.station[index]["Vk"] = 0
        self.station[index]["Qj"] = "init"
        self.station[index]["Qk"] = "init"
        self.station[index]["dest"] = 0
        self.station[index]["A"] = 0
        self.station[index]["status"] = "init"