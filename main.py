def intLimit(number):
    return number % 256

def regCheck(number, line):
    if number > 3:
        raise ValueError(f"""Invalid register number "{number}" on line {line}""")
    else:
        return number

class program:
    def __init__(self):
        self.binary = "program.psm"
        self.program = "code.psms"
        self.compiled = b""


    def compile(self):
        with open(self.program, "r") as file:
            code = file.read()
            file.close()

        code = code.split("\n")
        #compiled = b""


        def append(number):
            self.compiled += number.to_bytes(1, "big")


        for line in range(len(code)):
            x = code[line].split(" ")
            print(x)

            # move to
            if x[0] == "mvt":
                value = intLimit(int(x[1]))
                registerTo = regCheck(intLimit(int(x[2])),line)
                append(1)
                append(value)
                append(registerTo)

            # move from
            elif x[0] == "mvf":
                registerFrom = regCheck(intLimit(int(x[1])),line)
                index = intLimit(int(x[2]))
                append(2)
                append(registerFrom)
                append(index)

            # move from one reg to another
            elif x[0] == "regmv":
                registerFrom = regCheck(intLimit(int(x[1])),line)
                registerTo = regCheck(intLimit(int(x[2])),line)
                append(3)
                append(registerFrom)
                append(registerTo)


            # add
            elif x[0] == "add":
                append(4)

            # subtract
            elif x[0] == "sub":
                append(5)

            # multiply
            elif x[0] == "mult":
                append(6)

            # divide
            elif x[0] == "div":
                append(7)

            # and
            elif x[0] == "and":
                append(8)

            # nand
            elif x[0] == "nand":
                append(9)

            # or
            elif x[0] == "or":
                append(10)

            # xor
            elif x[0] == "xor":
                append(11)

            # push
            elif x[0] == "push":
                append(12)

            # pop
            elif x[0] == "pop":
                append(13)

            # jump
            elif x[0] == "jmp":
                index = intLimit(int(x[1]))
                append(14)
                append(index)

            # jump if equal
            elif x[0] == "jmpe":
                index = intLimit(int(x[1]))
                append(15)
                append(index)

            # jump if not equal
            elif x[0] == "jmpne":
                index = intLimit(int(x[1]))
                append(16)
                append(index)

            # jump if less than
            elif x[0] == "jmpl":
                index = intLimit(int(x[1]))
                append(17)
                append(index)

            # jump if greater than
            elif x[0] == "jmpg":
                index = intLimit(int(x[1]))
                append(18)
                append(index)

        print(self.compiled)

        with open(self.binary, "wb") as file:
            file.write(self.compiled)


    def run(self):
        with open(self.binary, "rb") as file:
            memory = file.read()
            file.close()

        print(memory)
        reg = [0, 0, 0, 0]
        stack = []
        memoryList = list(memory)


        index = 0
        while index != len(memoryList):

            # move to register: 00000001
            if memoryList[index] == 1:
                value = intLimit(memoryList[index + 1])
                register = memoryList[index + 2]
                reg[register] = value
                index += 2

            # move from register: 00000010
            elif memoryList[index] == 2:
                register = memoryList[index + 1]
                i = memoryList[index + 2]
                memoryList[i] = reg[register]
                index += 2

            # move from one register to another: 00000011
            elif memoryList[index] == 3:
                registerFrom = memoryList[index + 1]
                registerTo = memoryList[index + 2]
                reg[registerTo] = reg[registerFrom]
                reg[registerFrom] = 0
                index += 2

            # add: 00000100
            elif memoryList[index] == 4:
                reg[2] = intLimit(reg[0] + reg[1])

            # subtract: 00000101
            elif memoryList[index] == 5:
                reg[2] = intLimit(reg[0] - reg[1])

            # multiply: 00000110
            elif memoryList[index] == 6:
                reg[2] = intLimit(reg[0] * reg[1])

            # divide: 00000111
            elif memoryList[index] == 7:
                reg[2] = intLimit(reg[0] // reg[1])

            # and: 00001000
            elif memoryList[index] == 8:
                reg[2] = reg[0] & reg[1]

            # nand: 00001001
            elif memoryList[index] == 9:
                reg[2] = reg[0] & reg[1]
                reg[2] = ~ reg[2]

            # or: 00001010
            elif memoryList[index] == 10:
                reg[2] = reg[0] | reg[1]

            # xor: 00001011
            elif memoryList[index] == 11:
                reg[2] = reg[0] ^ reg[1]

            # push: 00001100
            elif memoryList[index] == 12:
                stack.append(reg[3])

            # pop: 00001101
            elif memoryList[index] == 13:
                reg[3] = stack.pop(len(stack)-1)

            # jump: 00001110
            elif memoryList[index] == 14:
                index = memoryList[index + 1]

            # jump if equal: 00001111
            elif memoryList[index] == 15:
                if reg[0] == reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            # jump if not equal: 00010000
            elif memoryList[index] == 16:
                if reg[0] != reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            # jump if less than: 00010001
            elif memoryList[index] == 17:
                if reg[0] < reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            # jump if greater than: 00010001
            elif memoryList[index] == 18:
                if reg[0] > reg[1]:
                    index = memoryList[index + 1]
                else:
                    index += 1

            index += 1

            print(f"registers: {reg}")
            print(f"stack: {stack}")
        print(f"memory: {memoryList}")

run = program()
run.compile()
run.run()