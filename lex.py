from util import *
from Token import keywords, Tokens
symbol_table = []
symbol_table.extend(keywords)

def lex_result(input_token,  value=None):
        token_type = Tokens(input_token).name
        if(not value):
            return {
            "token":token_type
            }
        elif(input_token == "int"):
            return {
                "token": token_type,
                "integer_value": value
            }
        elif(input_token == "float"):
            return {
                "token": token_type,
                "float_value": value
            }
        if(input_token == "err"):
            return {
                "token": token_type,
                "unrecognized_string": value
            }
        elif(input_token == "id"):
            return {
                "token": token_type,
                "index": value
            }
def add_to_symbol_table(identifier):
    if(symbol_table.count(identifier)):
        return symbol_table.index(identifier)
    else:
        symbol_table.append(identifier)
        return symbol_table.index(identifier)

def print_symbol_table():
    return "Symbol Table:  " + str(symbol_table)
    
def lex(input_token):
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



