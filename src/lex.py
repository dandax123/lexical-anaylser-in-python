from util import *
from Token import keywords, Tokens
symbol_table = []
symbol_table.extend(keywords)

def lex_result(input_token,  value=None):
    return value
def add_to_symbol_table(identifier):
    if(symbol_table.count(identifier)):
        return symbol_table.index(identifier)
    else:
        symbol_table.append(identifier)
        return symbol_table.index(identifier)

def print_symbol_table():
    return "Symbol Table:  " + str(symbol_table)
    
def _lex(input_token):
    if(is_operator(input_token)):
        return lex_result(input_token)
    elif(is_identifier(input_token)):
        index = add_to_symbol_table(input_token)
        return lex_result(input_token = "id", value= index)
    elif(is_keyword(input_token)):
        return lex_result(input_token)
    elif(is_integer(input_token)):
        x = int(input_token)
        return lex_result(input_token="int", value=x)
    elif(is_float(input_token)):
        x = float(input_token)
        return lex_result(input_token="float", value=x)
    else:
        return lex_result(input_token="err", value=input_token)



