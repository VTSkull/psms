# Docs:

## Basic info
psm(python assembly) is a machine-code-like language I made in a day. psm has 6 registers that range from 0 to 5. register 0 is used for writing to stdout and register 1 is used for reading stdin. psms(python assembly script) is a assembly-like language that gets compiled into psm. This is the documentation for psms

## Instructions:

### mvt
Moves a value to a register.

Usage:

`mvt <value> <register>`

---
### mvm
Moves a value from memory into a register

Usage:

`mvm <index> <register>`

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
Adds the number in register 2 with register 3 and returns it to register 4

Usage:

`add`

---
### sub
Subtracts the number in register 2 with register 3 and returns it to register 4

Usage:

`sub`

---
### mult
Multiplies the number in register 2 with register 3 and returns it to register 4

Usage:

`mult`

---
### div
Divides the number in register 2 with register 3 and returns it to register 4

Usage:

`div`

---
### and
Does bitwise and on the value in register 2 and register 3 and returns it to register 4

Usage:

`and`

---
### nand
Does bitwise nand on the value in register 2 and register 3 and returns it to register 4

Usage:

`nand`

---
### or

Does bitwise or on the value in register 2 and register 3 and returns it to register 4

Usage:

`or`

---
### xor
Does bitwise xor on the value in register 2 and register 3 and returns it to register 4

Usage:

`xor`

---
### push
Pushes the value in register 5 to the stack

Usage:

`push`

---
### pop
Pops the value of the top of the stack and returns it to register 5

Usage:

`pop`

---
### jmp
Jumps to the index specified in the parameter

Usage:

`jmp <index>`

---
### jmpe
Jumps to the index specified in the parameter if the value in register 2 and register 3 are equal

Usage:

`jmpe <index>`

---
### jmpn
Jumps to the index specified in the parameter if the value in register 2 and register 3 are not equal

Usage:

`jmpn <index>`

---
### jmpl
Jumps to the index specified in the parameter if the value in register 2 is less than the value in register 3

Usage:

`jmpl <index>`

---
### jmpg
Jumps to the index specified in the parameter if the value in register 2 is greater than the value in register 3

Usage:

`jmpg <index>`

---
### label
Defines a label to jump to. Can be used in a jump instruction as the index

Usage:

`:<label_name>`

`jmp :<label_name>`

---
### mem
creates blank bytes for length then jumps over them

Usage:

`mem <length>`