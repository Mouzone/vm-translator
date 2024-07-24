# translate hack VM language to hack ASM language
def parseOperations(operation):
    return


def parsePushPop(args):
    return


def parseLine(line):
    args = line.split(" ")
    if len(args) == 1:
        # add, sub, neg, eq, gt, lt, and, or, not
        # "ng" and "not" only change the recent elements
        parseOperations(args[0])
    else:
        # push, pop
        # args[0] -> push/pop
        # args[1] -> memory segment
        # args[2] -> memory segment's index
        # ex) push local 2 => @LCL + 2
        # ex) push constant 42 => @42
        # ex) push argument 1 => @ARG + 1
        parsePushPop(args)


def parseFile():
    test_folder_path = "test files/"
    file_name = input("File to translate: ")
    file = open(f"{test_folder_path}{file_name}/{file_name}.vm", "r")
    for line in file:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("//"):
            print(stripped_line)
            # parseLine(line)

parseFile()