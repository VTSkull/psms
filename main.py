def intLimit(number):
    return number % 256

def regCheck(number, line):
    if number > 3:
        raise ValueError(f"""Invalid register number "{number}" on line {line}""")
    else:
        return number

class program:
    def __init__(self):
        self.debug = False

        self.binary = "program.psm"
        self.program = "code.psms"
        self.precompiled = []
        self.compiled = b""


    def compile(self):
        with open(self.program, "r") as file:
            code = file.read()
            file.close()

        code = code.split("\n")
        labels = {}
        labelJumps = {}

        def finalCompile():
            for x in self.precompiled:
                self.compiled += int(x).to_bytes(1, "big")

        def append(number):
            self.precompiled.append(number)


        for line in range(len(code)):
            x = code[line].split(" ")

            # move to
            if x[0] == "mvt":
                value = intLimit(int(x[1]))
                registerTo = regCheck(intLimit(int(x[2])),line)
                append(1)
                append(value)
                append(registerTo)

            #move from memory
            elif x[0] == "mvm":
                index = x[1]
                append(2)
                append(index)

            # move from
            elif x[0] == "mvf":
                registerFrom = regCheck(int(x[1]),line)
                index = intLimit(int(x[2]))
                append(3)
                append(registerFrom)
                append(index)

            # move from one reg to another
            elif x[0] == "regmv":
                registerFrom = regCheck(intLimit(int(x[1])),line)
                registerTo = regCheck(intLimit(int(x[2])),line)
                append(4)
                append(registerFrom)
                append(registerTo)

            # add
            elif x[0] == "add":
                append(5)

            # subtract
            elif x[0] == "sub":
                append(6)

            # multiply
            elif x[0] == "mult":
                append(7)

            # divide
            elif x[0] == "div":
                append(8)

            # and
            elif x[0] == "and":
                append(9)

            # nand
            elif x[0] == "nand":
                append(10)

            # or
            elif x[0] == "or":
                append(11)

            # xor
            elif x[0] == "xor":
                append(12)

            # push
            elif x[0] == "push":
                append(13)

            # pop
            elif x[0] == "pop":
                append(14)

            # jump
            elif x[0] == "jmp":
                append(15)
                if x[1][0] == ":":
                    index = x[1]
                    append(0)
                    labelJumps[index] = len(self.precompiled)-1
                else:
                    index = intLimit(int(x[1]))
                    append(index)

            # jump if equal
            elif x[0] == "jmpe":
                append(16)
                if x[1][0] == ":":
                    index = x[1]
                    append(0)
                    labelJumps[index] = len(self.precompiled)-1
                else:
                    index = intLimit(int(x[1]))
                    append(index)

            # jump if not equal
            elif x[0] == "jmpne":
                append(17)
                if x[1][0] == ":":
                    index = x[1]
                    append(0)
                    labelJumps[index] = len(self.precompiled)-1
                else:
                    index = intLimit(int(x[1]))
                    append(index)

            # jump if less than
            elif x[0] == "jmpl":
                append(18)
                if x[1][0] == ":":
                    index = x[1]
                    append(0)
                    labelJumps[index] = len(self.precompiled)-1
                else:
                    index = intLimit(int(x[1]))
                    append(index)

            # jump if greater than
            elif x[0] == "jmpg":
                append(19 )
                if x[1][0] == ":":
                    index = x[1]
                    append(0)
                    labelJumps[index] = len(self.precompiled)-1
                else:
                    index = intLimit(int(x[1]))
                    append(index)

            # label
            elif x[0][0] == ":":
                if len(self.precompiled) == 0:
                    labels[x[0]] = len(self.precompiled)
                else:
                    labels[x[0]] = len(self.precompiled) - 1

            # memory
            elif x[0] == "mem":
                length = intLimit(int(x[1]))
                append(15)
                append(len(self.precompiled) + int(length))
                for y in range(length):
                    append(0)



        for y in labelJumps:
            goto = labels[y]
            self.precompiled[labelJumps[y]] = goto

        if self.debug:
            print(self.precompiled)
            print(self.compiled)
            print(labels)
            print(labelJumps)
        finalCompile()
        with open(self.binary, "wb") as file:
            file.write(self.compiled)


    def run(self):
        with open(self.binary, "rb") as file:
            memory = file.read()
            file.close()

        #print(memory)
        reg = [0, 0, 0, 0]
        stack = []
        memoryList = list(memory)


        index = 0
        while index <= len(memoryList) - 1:

            print(f"registers: {reg}")
            print(f"stack: {stack}")
            print(f"index: {index}")

            # move to register: 00000001
            if memoryList[index] == 1:
                value = intLimit(memoryList[index + 1])
                register = memoryList[index + 2]
                reg[register] = value
                index += 2

            # move from memory to register: 00000010
            elif memoryList[index] == 2:
                value = memoryList[memoryList[index + 1]]
                register = memoryList[index + 2]
                reg[register] = value
                index += 2


            # move from register: 00000011
            elif memoryList[index] == 3:
                register = memoryList[index + 1]
                i = memoryList[index + 2]
                memoryList[i] = reg[register]
                index += 2

            # move from one register to another: 00000100
            elif memoryList[index] == 4:
                registerFrom = memoryList[index + 1]
                registerTo = memoryList[index + 2]
                reg[registerTo] = reg[registerFrom]
                reg[registerFrom] = 0
                index += 2

            # add: 00000101
            elif memoryList[index] == 5:
                reg[2] = intLimit(reg[0] + reg[1])

            # subtract: 00000110
            elif memoryList[index] == 6:
                reg[2] = intLimit(reg[0] - reg[1])

            # multiply: 00000111
            elif memoryList[index] == 7:
                reg[2] = intLimit(reg[0] * reg[1])

            # divide: 00001000
            elif memoryList[index] == 8:
                reg[2] = intLimit(reg[0] // reg[1])

            # and: 00001001
            elif memoryList[index] == 9:
                reg[2] = reg[0] & reg[1]

            # nand: 00001010
            elif memoryList[index] == 10:
                reg[2] = reg[0] & reg[1]
                reg[2] = ~ reg[2]

            # or: 00001011
            elif memoryList[index] == 11:
                reg[2] = reg[0] | reg[1]

            # xor: 00001100
            elif memoryList[index] == 12:
                reg[2] = reg[0] ^ reg[1]

            # push: 00001101
            elif memoryList[index] == 13:
                stack.append(reg[3])

            # pop: 00001110
            elif memoryList[index] == 14:
                reg[3] = stack.pop(len(stack)-1)

            # jump: 00001111
            elif memoryList[index] == 15:
                index = memoryList[index + 1]

            # jump if equal: 00010000
            elif memoryList[index] == 16:
                if reg[0] == reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            # jump if not equal: 00010001
            elif memoryList[index] == 17:
                if reg[0] != reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            # jump if less than: 00010001
            elif memoryList[index] == 18:
                if reg[0] < reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            # jump if greater than: 
            elif memoryList[index] == 19:
                if reg[0] > reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            index += 1

            
        print(f"memory: {memoryList}")

run = program()
run.compile()
run.run()