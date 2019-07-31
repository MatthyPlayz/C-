import re

class Lexer:
    loops = ["for", "while", "forever"]
    cout = ["println", "print", "newl"]
    cin = ["input", "inputln"]
    tokensa = [loops, cin,cout]
    white_space = ' '
    def lex(code,tokenlista=tokensa,white_space=white_space):
        output = []
        lexeme = ""
        for i,char in enumerate(code):
            lexeme += char # adding a char each time
            if (i+1 < len(code)): # prevents error
                if code[i+1] == white_space: # if next char == ' '
                    output.append(lexeme)
                    lexeme = ''
        output.append(lexeme)
        for i in range(0,len(output)):
            output[i] = output[i].replace(" ", "") # Remove spaces
        return output # Output the "output" list
