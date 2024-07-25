# translate hack VM language to hack ASM language
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
        output.append("@evaluate")
        output.append(f"D;{jump_functions[operation]}")

        output.append("@0")
        output.append("D=A")
        output.append("@SP")
        output.append("A=M")
        output.append("M=D")
        output.append("@increment")
        output.append("0;JMP")

        output.append("(EVALUATE)")
        output.append("@0")
        output.append("D=!A")
        output.append("@SP")
        output.append("A=M")
        output.append("M=D")

        output.append("(INCREMENT)")
        output.append("@SP")
        output.append("M=M+1")

def parsePushPop(args, output):
    return


def parseLine(line ,output):
    args = line.split(" ")
    if len(args) == 1:
        # add, sub, neg, eq, gt, lt, and, or, not
        # "ng" and "not" only change the recent elements
        parseOperations(args[0], output)
    else:
        # push, pop
        # args[0] -> push/pop
        # args[1] -> memory segment
        # args[2] -> memory segment's index
        # ex) push local 2 => @LCL + 2
        # ex) push constant 42 => @42
        # ex) push argument 1 => @ARG + 1
        parsePushPop(args, output)


def parseFile():
    test_folder_path = "test files/"
    file_name = input("File to translate: ")
    file = open(f"{test_folder_path}{file_name}/{file_name}.vm", "r")

    output = []
    for line in file:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("//"):
            parseLine(line, output)

    printOutput(output, file_name)


def printOutput(output, file_name):
    return


parseFile()
