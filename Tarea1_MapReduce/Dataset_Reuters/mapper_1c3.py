import sys
import re

tag = "TEXT"
acumulando = False
parrafo = ""
indice = 1

def get_text(text, tag):
    reg = "<" + tag + ">(.*?)</" + tag + ">"
    body = re.findall(reg, text)
    #supone que solo hay un match
    if len(body)>0 and len(body[0])>0:
        return body[0]
    return "vacio"
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
   

    if line.find("<REUTERS") != -1:
        acumulando = True
        indice += 1
        parrafo = ""
        line = line[line.find("<REUTERS"):]
    if line.find("</REUTERS>") != -1:
        acumulando = False
        line = line[:line.find("</REUTERS>")]
        # split the line into words
        parrafo = parrafo + " " + line
        body = get_text(parrafo, "BODY")
        pais = get_text(parrafo, "PLACES")
        
        words = body.split()
        longitud =len(words)
        print('%s\t%s' % (longitud, pais))
        #print(parrafo)
    
    if acumulando:
        parrafo = parrafo + " " +line
        continue