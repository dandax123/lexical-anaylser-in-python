from Token import keywords, operators

def is_identifier(input_token):
    if(keywords.count(input_token)>0):
        return False
    elif(input_token[0].isalpha()):
        return True
    else:
        return False
def is_keyword(input_token):
    return bool(keywords.count(input_token))
def is_operator(input_token):
    return bool(operators.count(input_token))
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def is_float(n):
    try:
        int_n = int(n)
    except ValueError:
        try:
            float_b = float(n)
        except ValueError:
            return False
        else:
            return True
    else:
        return False




