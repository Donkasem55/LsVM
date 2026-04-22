import argparse, sys

parser = argparse.ArgumentParser(description="Open-source Bytecode VM")
parser.add_argument("run", help="Bytecode to run")

args = parser.parse_args()

instr = {
        0x00: "mov",
        0x01: "add",
        0x02: "sub",
        0x03: "mul",
        0x04: "div",
        0x05: "exp",
        0x06: "jmp",
        0x07: "call",
        0x08: "int",

        0x10: "EOF"
}

insargs = {
        "0": ["EOF"],
        "1": ["jmp", "call", "int"],
        "2": ["mov", "add", "sub", "mul", "div", "exp"]
}

with open(args.run, "rb") as f:
    data = f.read()
    if data[-1] != 0x10:
        print("File not executable or broken bytecode signature (exit code 10)")
        sys.exit(10)

data = list(data)
entry = data[0]

registers = {0x00: 0x0000, 0x01: 0x0000}

i = entry
while True:
    ins = instr[data[i]]
    if ins == "EOF":
        break

    if ins in insargs["2"]:
        opr = [data[i]]
        opr.append(data[i+1])
        opr.append(data[i+2])
        i += 3
        if opr[0] == 0x00:
            if opr[1] in registers:
                registers[opr[1]] = opr[2]

        continue
    
    if ins in insargs["1"]:
        opr = [data[i]]
        opr.append(data[i+1])
        i += 2

        if opr[0] == 0x08:
            if opr[1] == 0x10:
                if registers[0x01] == 0x00:
                    j = registers[0x00]
                    while data[j] != 0x00:
                        print(chr(data[j]), end="")
                        j += 1

        continue

    elif ins in insargs["0"]:
        if ins == "EOF":
            break
        i += 1

