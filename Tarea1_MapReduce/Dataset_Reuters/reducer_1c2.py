from operator import itemgetter
import sys

longest_word = ""
title_date = ""

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, title = line.split('\t', 1)
    if (len(word) > len(longest_word)):
        longest_word = word
        title_date = title

    
  


print ('%s\t%s' % (longest_word, title_date))