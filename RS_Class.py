class RS:
    def __init__(self, station_config):
        self.station_config = station_config
        self.index = {}
        self.index["lw"] = 0
        self.index["sw"] = self.index["lw"] + self.station_config["lw_num"]
        self.index["jmp"] = self.index["sw"] + self.station_config["sw_num"]
        self.index["jalr"] = self.index["sw"] + self.station_config["sw_num"]
        self.index["ret"] = self.index["sw"] + self.station_config["sw_num"]
        self.index["beq"] = self.index["jmp"] + self.station_config["jmp_num"]
        self.index["add"] = self.index["beq"] + self.station_config["beq_num"]
        self.index["sub"] = self.index["beq"] + self.station_config["beq_num"]
        self.index["addi"] = self.index["beq"] + self.station_config["beq_num"]
        self.index["nand"] = self.index["add"] + self.station_config["add_num"]
        self.index["mult"] = self.index["nand"] + self.station_config["nand_num"]

        self.used = {}
        self.used["lw"] = 0
        self.used["sw"] = 0
        self.used["jmp"] = 0
        self.used["beq"] = 0
        self.used["add"] = 0
        self.used["nand"] = 0
        self.used["mult"] = 0

        self.station = []

        for i in range(self.station_config["lw_num"]):
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
            self.station.append(station_entry)

        for i in range(self.station_config["sw_num"]):
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
            self.station.append(station_entry)

        for i in range(self.station_config["jmp_num"]):
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
            self.station.append(station_entry)

        for i in range(self.station_config["beq_num"]):
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
            self.station.append(station_entry)

        for i in range(self.station_config["add_num"]):
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
            self.station.append(station_entry)

        for i in range(self.station_config["nand_num"]):
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
            self.station.append(station_entry)

        for i in range(self.station_config["mult_num"]):
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
            self.station.append(station_entry)

    def update_station(self, name, index, busy, op, Vj, Vk, Qj, Qk, dest, A):
        self.station[self.index[name] + index]["busy"] = busy
        self.station[self.index[name] + index]["op"] = op
        self.station[self.index[name] + index]["Vj"] = Vj
        self.station[self.index[name] + index]["Vk"] = Vk
        self.station[self.index[name] + index]["Qj"] = Qj
        self.station[self.index[name] + index]["Qk"] = Qk
        self.station[self.index[name] + index]["dest"] = dest
        self.station[self.index[name] + index]["A"] = A

    def issue(self, name, Vj, Vk, Qj, Qk, dest, A):
        index = self.used["add"] if (name == "add" or name == "sub" or name == "addi") else self.used["jmp"] if (name == "jmp" or name == "jalr" or name == "ret") else self.used[name]
        self.station[self.index[name] + index]["busy"] = True
        self.station[self.index[name] + index]["op"] = name
        self.station[self.index[name] + index]["Vj"] = Vj if (Qj == None) else 0
        self.station[self.index[name] + index]["Vk"] = Vk if (Qj == None) else 0
        self.station[self.index[name] + index]["Qj"] = 0 if (Qj == None) else Qj
        self.station[self.index[name] + index]["Qk"] = 0 if (Qk == None) else Qk
        self.station[self.index[name] + index]["dest"] = dest
        self.station[self.index[name] + index]["A"] = A

        if (name == "add" or name == "sub" or name == "addi"):
            self.used["add"] += 1
        elif (name == "jmp" or name == "jalr" or name == "ret"):
            self.used["jmp"] += 1
        else:
            self.used[name] += 1

        #availabel with type