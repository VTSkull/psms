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

    # move to register: 00000001
    if memoryList[index] == 1:
        value = memoryList[index + 1]
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
        reg[2] = reg[0] + reg[1]

    # subtract: 00000101
    elif memoryList[index] == 5:
        reg[2] = reg[0] - reg[1]

    # multiply: 00000110
    elif memoryList[index] == 6:
        reg[2] = reg[0] * reg[1]

    # divide: 00000111
    elif memoryList[index] == 7:
        reg[2] = reg[0] // reg[1]

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