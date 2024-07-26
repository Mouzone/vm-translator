iteration = 0
def parseOperations(operation, output):
    two_argument_functions = {
        "add": "+",
        "sub": "-",
        "and": "&",
        "or": "|",
    }

    one_argument_functions = {
        "neg": "-",
        "not": "!"
    }

    jump_functions = {
        "eq": "JEQ",
        "gt": "JGT",
        "lt": "JLT",
    }

    if operation in two_argument_functions.keys():
        output.append("@SP")
        output.append("M=M-1")
        output.append("A=M")
        output.append("D=M")
        output.append("@SP")
        output.append("A=M")
        output.append(f"A=M${two_argument_functions[operation]}D")

    if operation in one_argument_functions.keys():
        output.append("@SP")
        output.append("A=M-1")
        output.append("D=M")
        output.append(f"M={one_argument_functions[operation]}D")

    if operation in jump_functions.keys():
        output.append("@SP")
        output.append("M=M-1")
        output.append("A=M")
        output.append("D=M")

        output.append("@SP")
        output.append("M=M-1")
        output.append("A=M")
        output.append("D=M")
        output.append(f"@evaluate_{iteration}")
        output.append(f"D;{jump_functions[operation]}")

        output.append("@0")
        output.append("D=A")
        output.append("@SP")
        output.append("A=M")
        output.append("M=D")
        output.append(f"@increment_{iteration}")
        output.append("0;JMP")

        output.append(f"(EVALUATE_{iteration})")
        output.append("@0")
        output.append("D=!A")
        output.append("@SP")
        output.append("A=M")
        output.append("M=D")

        output.append(f"(INCREMENT_{iteration})")
        output.append("@SP")
        output.append("M=M+1")

def parsePushPop(args, output, filename):
    standard = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT",
    }
    if args[0] == "push":
        if args[1] in standard.keys():
            output.append(f"@{args[2]}")
            output.append("D=A")
            output.append(f"@{args[1]}")
            output.append("A=M+D")
            output.append("D=M")
        else:
            if args[1] == "constant":
                output.append(f"@{args[2]}")
            if args[1] == "static":
                output.append(f"@{filename}.{args[2]}")
            if args[1] == "temp":
                output.append(f"@{5 + args[2]}")
            if args[1] == "pointer":
                if args[2] == 0:
                    output.append(f"@{3}")
                else:
                    output.append(f"@{4}")
                output.append("A=M")
        output.append("D=A")
        output.append("@SP")
        output.append("A=M")
        output.append("M=D")
        output.append("@SP")
        output.append("M=M+1")
    else:


def parseLine(line, output, filename):
    args = line.split(" ")
    if len(args) == 1:
        parseOperations(args[0], output)
    else:
        parsePushPop(args, output, filename)


def parseFile():
    test_folder_path = "test files/"
    file_name = input("File to translate: ")
    file = open(f"{test_folder_path}{file_name}/{file_name}.vm", "r")

    output = []
    for line in file:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("//"):
            parseLine(line, output, file_name)

    printOutput(output, file_name)


def printOutput(output, file_name):
    return


parseFile()
