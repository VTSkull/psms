# Docs:

## Basic info
psm(python assembly) is a machine-code-like language I made in a day. psm has 4 addresses that range from 0 to 3. psms(python assembly script) is a assembly-like language that gets compiled into psm. This is the documentation for psms

## Instructions:

### mvt
Moves a value to a register.
Usage:
`mvt <value> <register>`

---
### mvf
Moves a value from a register into program memory
Usage:
`mvf <register> <index>`

---
### regmv
Moves a value from one register to another
Usage:
`regmv <register_from> <register_to>`

---
### add
Adds the number in register 0 with register 1 and returns it to register 2
Usage:
`add`

---
### sub
Subtracts the number in register 0 with register 1 and returns it to register 2
Usage:
`sub`

---
### mult
Multiplies the number in register 0 with register 1 and returns it to register 2
Usage:
`mult`

---
### div
Divides the number in register 0 with register 1 and returns it to register 2
Usage:
`div`

---
### and
Does bitwise and on the value in register 0 and register 1 and returns it to register 2
Usage:
`and`

---
### nand
Does bitwise nand on the value in register 0 and register 1 and returns it to register 2
Usage:
`nand`

---
### or

Does bitwise or on the value in register 0 and register 1 and returns it to register 2
Usage:
`or`

---
### xor
Does bitwise xor on the value in register 0 and register 1 and returns it to register 2
Usage:
`xor`

---
### push
Pushes the value in register 3 to the stack
Usage:
`push`

---
### pop
Pops the value of the top of the stack and returns it to register 3
Usage:
`pop`
