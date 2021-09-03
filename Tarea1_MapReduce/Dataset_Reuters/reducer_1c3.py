from operator import itemgetter
import sys

longest_word = 0
country = ""

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    longitud, pais = line.split('\t', 1)

    try:
        longitud = int(longitud)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if (longitud > longest_word):
        longest_word = longitud
        country = pais

    
  


print ('%s\t%s' % (longest_word, country))