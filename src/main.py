from File import File
from lex import  print_symbol_table, _lex
print("Lexical anaylser and parser in python")
input_token_index = -1
input_tokens = ""
userAction = 0
shouldExit = False
next_token = '$'
error = False

print("\n")
def lex():
    global next_token
    global input_token_index
    input_token_index = input_token_index + 1
    next_token = input_tokens[input_token_index]
    if(next_token.isspace()):
        lex()
def unconsumed_input():
    return 'calll'
class Parser:
    def __init__(self):
        global error
        global next_token
        print("Starting the parser ... \n")
        self.G()
    def G(self):
        global error
        global next_token
        lex()
        print("G -> E")
        self.E()
        if (next_token =='$' and (not error)):
            print("success")
        else:
            print("failure: unconsumed input " +  unconsumed_input())
    #/* E -> T R */
    def E(self):
        global error
        global next_token
        if ( error):
            return None
        print("E -> T R")
        self.T()
        self.R()
    #/* R -> + T R | - T R | e */
    def R(self):
        global error
        global next_token
        if (error):
            return None 
        if (next_token == '+'):
            print("R -> + T R")
            lex()
            self.T()
            self.R()
        elif (next_token == '-'):
            print("R -> - T R")
            lex()
            self.T()
            self.R()
        else:
            print("R->e")
    #/* T -> F S */
    def T(self):
        global error
        global next_token
        if (error):
            return None
        print("T -> F S")
        self.F()
        self.S()
    #/* S -> * F S | / F S | e */
    def S(self):
        global error
        global next_token
        if (error):
            return None
        if (next_token=='*'):
            print("S -> * F S")
            lex()
            self.F()
            self.S()
        elif (next_token=='/'):
            print("S -> / F S")
            lex()
            self.F()
            self.S()
        else:
            print("S -> e")
    #/* F -> ( E ) | N */
    def F(self):
        global error
        global next_token
        if (error):
            return None
        if (next_token=='(' ):
            print("F->( E )")
            lex()
            self.E()
            if (next_token == ')' ):
                lex()   
            else:
                error=True
                print("error: unexptected token " + next_token) 
                print("unconsumed_input "+ unconsumed_input())
                return None
        elif (next_token in ['a' , 'b' , 'c' , 'd']):
            print("F->M")
            self.M() 
        elif (next_token in ['0' , '1' , '2' , '3']):
            print("F->N")
            self.N()    
        else:
            error=True
            print("error: unexptected token " + next_token)
            print("unconsumed_input "+ unconsumed_input())
    #/* M  a | b | c | d */
    def M(self):
        global error
        global next_token
        if (error):
            return None
        if (next_token in ['a' , 'b' , 'c' , 'd']):
            print("M->" + next_token)
            lex()
        else:
            error=True
            print("error: unexptected token " + next_token)
            print("unconsumed_input "+ unconsumed_input())
        

    #/* N  0 | 1 | 2 | 3 */
    def N(self):
        global error
        global next_token
        if (error):
            return None
        if (next_token in ['0' , '1' , '2' , '3']):
            print("N->" + next_token)
            lex()
        else :
            error=True
            print("error: unexptected token " + next_token) 
            print("unconsumed_input "+ unconsumed_input())
 



while(not shouldExit):
    print("1. Enter filename \n")
    print("2. Exit \n")
    userAction = int(input("Enter the action to  be performed: "))
    if(userAction == 1):
        input_token_index = -1
        inputFile = File("test.txt")
        input_tokens = inputFile.read_input_token()
        myparser = Parser()
    elif(userAction == 3):
        shouldExit = True
