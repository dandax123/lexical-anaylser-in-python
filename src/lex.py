def unconsumed_input():
    return 'calll'

def lex():
    global next_token
    global input_token_index
    input_token_index = input_token_index + 1
    self.next_token = input_tokens[input_token_index]
    if(next_token.isspace()):
        lex()