with open("program.psm", "rb") as file:
    memory = file.read()
    file.close()

print(memory)
reg = [0, 0, 0, 0]
stack = []
memoryList = list(memory)


#for x in memory:
#    print(x)
#    memoryList.append(ord(x))


index = 0
while index != len(memoryList):

    # move to register: 0001
    if memoryList[index] == 1:
        value = memoryList[index + 1]
        register = memoryList[index + 2]
        reg[register] = value
        index += 2

    # move from register: 0010
    elif memoryList[index] == 2:
        register = memoryList[index + 1]
        i = memoryList[index + 2]
        memoryList[i] = reg[register]
        index += 2

    # move from one register to another: 0011
    elif memoryList[index] == 3:
        registerFrom = memoryList[index + 1]
        registerTo = memoryList[index + 2]
        reg[registerTo] = reg[registerFrom]
        reg[registerFrom] = 0
        index += 2

    # add: 0100
    elif memoryList[index] == 4:
        reg[2] = reg[0] + reg[1]

    # subtract: 0101
    elif memoryList[index] == 5:
        reg[2] = reg[0] - reg[1]

    # multiply: 0110
    elif memoryList[index] == 6:
        reg[2] = reg[0] * reg[1]

    # divide: 0111
    elif memoryList[index] == 7:
        reg[2] = reg[0] // reg[1]

    # and: 1000
    elif memoryList[index] == 8:
        reg[2] = reg[0] & reg[1]

    # nand: 1001
    elif memoryList[index] == 9:
        reg[2] = reg[0] & reg[1]
        reg[2] = ~ reg[2]

    # or: 1010
    elif memoryList[index] == 10:
        reg[2] = reg[0] | reg[1]

    # xor: 1011
    elif memoryList[index] == 11:
        reg[2] = reg[0] ^ reg[1]

    # push: 1100
    elif memoryList[index] == 12:
        stack.append(reg[3])

    # pop: 1101
    elif memoryList[index] == 13:
        reg[3] = stack.pop(len(stack)-1)

    index += 1

    print(f"registers: {reg}")
    print(f"stack: {stack}")
print(f"memory: {memoryList}")