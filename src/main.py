from File import File
from Parser import Node, initializeParse, printTree, evaluate, globals
print("Lexical anaylser and parser in python")
userAction = 0
shouldExit = False
print("\n")

while(not shouldExit):
    print("1. Enter filename \n")
    print("2. Exit \n")
    userAction = int(input("Enter the action to  be performed: "))
    if(userAction == 1):
        inputFile = File(input("Enter the filename: "))
        input_tokens = inputFile.read_input_token()
        initializeParse(input_tokens)
        theTree = Node().G()
        if(globals['error'] == False):
            printTree(theTree)
            value = evaluate(theTree)
            print("The calculated value is " + str(value))
        else:
            print("unsuccessful parsing")
        print("\n")
    elif(userAction == 2):
        shouldExit = True
