import enum
keywords = ["for", "while", "if", "else"]
operators = ["&&", "|", "||", "&"]
class Tokens(enum.Enum):
    FOR = 'for'     
    WHILE = 'while'
    IF = 'if'
    ELSE = 'else'
    INTEGER = 'int'
    FLOAT = 'float'
    BITWISE_OR = '|'
    LOGICAL_OR = '||'
    BITWISE_AND = '&'
    LOGICAL_AND = '&&'
    ID = 'id'
    ERROR = 'err'