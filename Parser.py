from Lexer import Lexer
class Data:
    true = True
    false = False
class Parser:
    loops = ["for", "while", "forever"]
    cout = ["println", "print", "newl"]
    cin = ["input", "inputln"]
    tokensa = [loops, cin,cout]
    def parse(code,tokenlista=tokensa):
        output = Lexer.lex(code)
        newl = "\n"
        try: # START VARIABLES
            if(output[1] == "=" and output[2] != None):
                exec("Data." + output[0] + "=" + output[2])
                return output[2]
        except(IndexError):
            pass # END VARIABLES
        
        for i in range(0,2): # START PRINT/PRINTLN
            if(i == 1 or i == 2):
                for x in range(0,1):
                    if(output[i] != tokenlista[i][x]):
                        if(output[i-1] == "println"):
                            mainout = ""
                            for l in range(0,len(output)):
                                mainout += " " + output[l]
                            for xa in range(len(Data.__dict__)):
                                if(output[xa+1] in Data.__dict__):
                                    code = compile("Data.temp = " + "Data." + output[1], "<string>", "exec")
                                    exec(code)
                                    return print(Data.temp, end='')
                                elif((output[xa+1][0:1] == "\"" and output[xa+1][len(output[xa+1])-1,len(output[xa+1])] == "\"") or (output[xa+1][0:1] == "\'" and output[xa+1][len(output[xa+1])-1,len(output[xa+1])] == "\'")):
                                    return print(mainout[9:len(mainout)] + "\n")
                        elif(output[i-1] == "print"):
                            mainout = ""
                            for l in range(0,len(output)):
                                mainout += output[l]
                            for xa in range(len(Data.__dict__)):
                                if(output[xa+1] in Data.__dict__):
                                    code = compile("Data.temp = " + "Data." + output[1], "<string>", "exec")
                                    exec(code)
                                    return print(Data.temp, end='')
                                else:
                                    return print(mainout[5:len(mainout)], end='') # END PRINT/PRINTLN
        print(i)
        
