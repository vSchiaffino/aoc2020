from copy import deepcopy

def main():
    code = getCode()
    accum = getAccum(code)
    # print(accum)
    for line in code:
        line["visited"] = False
    for i, line in enumerate(code):
        newCode = deepcopy(code)
        instr = line["instr"]
        newInstr = ""
        if instr == "jmp":
            newInstr = "nop"
        elif instr == "nop":
            newInstr = "jmp"
        else:
            continue
        newLine = deepcopy(line)
        newLine["instr"] = newInstr
        newCode[i] = newLine
        result = runProgram(newCode)
        if(result["ok"] == True):
            print(f"worked with accum {result['accum']}")

def runProgram(code):
    i = 0
    accum = 0
    while(1):
        if( i >= len(code)):
            return {'ok': True, 'accum': accum}
        line = code[i]
        if( line["visited"] == True ):
            return {'ok': False}
        line["visited"] = True
        instr = line["instr"]
        param = line["param"]
        if(instr == "jmp"):
            i += param
        else:
            if(instr == "acc"):
                accum += param
            i += 1

def getAccum(code):
    i = 0
    accum = 0
    while(code[i]["visited"] == False):
        line = code[i]
        line["visited"] = True
        instr = line["instr"]
        param = line["param"]
        if(instr == "jmp"):
            i += param
            continue
        elif(instr == "acc"):
            accum += param
        i += 1
    return accum


def getCode():
    code = []
    with open("input.in", "r") as f:
        lines = f.readlines()
        for line in lines:
            lineOfCode = {}
            parts = line.split(" ")
            instr = parts[0]
            parameter = int(parts[1])
            lineOfCode["instr"] = instr
            lineOfCode["param"] = parameter
            lineOfCode["visited"] = False   

            code.append(lineOfCode)         
    return code


if __name__ == "__main__":
    main()