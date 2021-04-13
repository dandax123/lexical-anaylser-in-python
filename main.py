from File import File
from lex import  print_symbol_table, lex

def handle_lex_result(lex_result):
    print("\n------------Lex information-----------------------")
    for x in lex_result.keys():
        print(x + ": " + str(lex_result[x]))
    print("--------------------------------------------------\n")
print("Lexical anaylser in python")
inputFile = File(input("Enter the file name: "))
input_tokens = inputFile.read_input_token()
input_token_index = -1
userAction = 0
shouldExit = False
print("\n")
while(not shouldExit):
    print("1. Call lex() \n")
    print("2. Show symbol table \n")
    print("3. Exit \n")
    userAction = int(input("Enter the action to  be performed: "))
    if(userAction == 1):
        input_token_index = input_token_index + 1
        try:
            lex_result = lex(input_tokens[input_token_index])
            handle_lex_result(lex_result)
        except IndexError:
            print("\nAll the tokens have been analysed \n")
            print(print_symbol_table())
            print("\n")    
    elif(userAction == 2):
        print(print_symbol_table())
    elif(userAction == 3):
        shouldExit = True
