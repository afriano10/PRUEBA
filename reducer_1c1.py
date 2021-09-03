from operator import itemgetter
import sys

total_words = 0
indiceFinal = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    indice, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    total_words += count
    indiceFinal = indice
  


print ('%s\t%s' % ("promedio", total_words/int(indiceFinal)))