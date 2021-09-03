from operator import itemgetter
import sys

total_words = 0
total_articles = 1

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
    total_articles += 1
  


print ('%s\t%s' % ("promedio", total_words/total_articles))