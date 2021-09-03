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
    return body[0]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    

    if line.find("<TEXT>") != -1:
        acumulando = True
        indice += 1
        parrafo = ""
        line = line[line.find("<TEXT>")+7:]
    if line.find("</TEXT>") != -1:
        acumulando = False
        line = line[:line.find("</TEXT>")]
        # split the line into words
        parrafo = parrafo + " " + line
        body = get_text(parrafo, "BODY")
        titulo = get_text(parrafo, "TITLE")
        fecha = get_text(parrafo, "DATELINE")
        
        words = body.split()
        longest_word = max(words, key=len)
        print('%s\t%s' % (longest_word, titulo + " " + fecha))
        #print(body)
    
    if acumulando:
        parrafo = parrafo + " " +line
        continue