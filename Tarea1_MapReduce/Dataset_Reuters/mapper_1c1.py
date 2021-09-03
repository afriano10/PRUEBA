import sys

tag = "TEXT"
acumulando = False
parrafo = ""
indice = 1

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    

    if line.find("<BODY>") != -1:
        acumulando = True
        indice += 1
        parrafo = ""
        line = line[line.find("<BODY>")+7:]
    if line.find("</BODY>") != -1:
        acumulando = False
        line = line[:line.find("</BODY>")]
        # split the line into words
        parrafo = parrafo + " " + line
        words = parrafo.split()
        print('%s\t%s' % (indice, len(words)))
        #print(parrafo)
    
    if acumulando:
        parrafo = parrafo + " " +line
        continue
    

    


    