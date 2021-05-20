class Parser:
    def __init__(self, input_tokens):
        print("Starting the parser ... \n")
        self.input_token_index = -1
        self.input_tokens = input_tokens
        self.error = False
        self.next_token = '$'
        self.G()
    def G(self):
        self.lex()
        print("G -> E")
        self.E()
        if (self.next_token =='$' and (not self.error)):
            print("success")
        else:
            print("failure: unconsumed input: " +  self.unconsumed_input())
    #/* E -> T R */
    def E(self):
        if (self.error):
            return None
        print("E -> T R")
        self.T()
        self.R()
    #/* R -> + T R | - T R | e */
    def R(self):
        if (self.error):
            return None 
        if (self.next_token == '+'):
            print("R -> + T R")
            self.lex()
            self.T()
            self.R()
        elif (self.next_token == '-'):
            print("R -> - T R")
            self.lex()
            self.T()
            self.R()
        else:
            print("R->e")
    #/* T -> F S */
    def T(self):
        if (self.error):
            return None
        print("T -> F S")
        self.F()
        self.S()
    #/* S -> * F S | / F S | e */
    def S(self):
        if (self.error):
            return None
        if (self.next_token=='*'):
            print("S -> * F S")
            self.lex()
            self.F()
            self.S()
        elif (self.next_token=='/'):
            print("S -> / F S")
            self.lex()
            self.F()
            self.S()
        else:
            print("S -> e")
    #/* F -> ( E ) | N */
    def F(self):
        if (self.error):
            return None
        if (self.next_token=='(' ):
            print("F->( E )")
            self.lex()
            self.E()
            if (self.next_token == ')' ):
                self.lex()   
            else:
                self.error=True
                print("error: unexpected token " + self.next_token) 
                return None
        elif (self.next_token in ['a' , 'b' , 'c' , 'd']):
            print("F->M")
            self.M() 
        elif (self.next_token in ['0' , '1' , '2' , '3']):
            print("F->N")
            self.N()    
        else:
            self.error=True
            print("error: unexpected token " + self.next_token)
    #/* M  a | b | c | d */
    def M(self):
        if (self.error):
            return None
        if (self.next_token in ['a' , 'b' , 'c' , 'd']):
            print("M->" + self.next_token)
            self.lex()
        else:
            self.error=True
            print("error: unexpected token " + self.next_token)
        

    #/* N  0 | 1 | 2 | 3 */
    def N(self):
        if (self.error):
            return None
        if (self.next_token in ['0' , '1' , '2' , '3']):
            print("N->" + self.next_token)
            self.lex()
        else :
            self.error=True
            print("error: unexpected token " + self.next_token) 
    
    def unconsumed_input(self):
        return self.input_tokens[self.input_token_index:]

    def lex(self):
        self.input_token_index = self.input_token_index + 1
        self.next_token = self.input_tokens[self.input_token_index]
        if(self.next_token.isspace()):
            self.lex()
 
