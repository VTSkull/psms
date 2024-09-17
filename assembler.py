with open("code.psms", "r") as file:
    code = file.read()
    file.close()

code = code.split("\n")
compiled = b""


def append(number):
    global compiled
    compiled += number.to_bytes(1, "big")


for line in code:
    x = line = line.split(" ")
    print(x)

    # move to
    if x[0] == "mvt":
        append(1)
        append(int(line[1]))
        append(int(line[2]))

    # move from
    elif x[0] == "mvf":
        append(2)
        append(int(line[1]))
        append(int(line[2]))

    # move from one reg to another
    elif x[0] == "regmv":
        registerFrom = x[1]
        registerTo = x[2]
        append(3)
        append(int(registerFrom))
        append(int(registerTo))


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
        index = x[1]
        append(14)
        append(int(index))

    # jump if equal
    elif x[0] == "jmpe":
        index = x[1]
        append(15)
        append(int(index))

    # jump if not equal
    elif x[0] == "jmpne":
        index = x[1]
        append(16)
        append(int(index))

    # jump if less than
    elif x[0] == "jmpl":
        index = x[1]
        append(17)
        append(int(index))

    # jump if greater than
    elif x[0] == "jmpg":
        index = x[1]
        append(18)
        append(int(index))

print(compiled)

with open("program.psm", "wb") as file:
    file.write(compiled)
