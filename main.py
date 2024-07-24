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
        "eq": "==",
        "gt": "",
        "lt": "",
    }

    if operation in two_argument_functions.keys():
        output.append("@SP")
        output.append("M=M-1")
        output.append("A=M")
        output.append("D=M")
        output.append("@SP")
        output.append("A=M")
        output.append(f"A=M${two_argument_functions[operation]}D")



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

parseFile()