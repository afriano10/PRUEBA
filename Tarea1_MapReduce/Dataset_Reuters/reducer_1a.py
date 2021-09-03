#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
max_count = 0
max_count2 = 0
max_count3 = 0
max_count4 = 0
max_count5 = 0
max_word2= None
max_word3= None
max_word4= None
max_word5= None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_count >= max_count:
            max_count= current_count 
            max_word = current_word
        elif current_count >= max_count -1:
            max_count2 = current_count
            max_word2 = current_word
        elif current_count >= max_count -2:
            max_count3 = current_count
            max_word3 = current_word
        elif current_count >= max_count -3:
            max_count4 = current_count
            max_word4 = current_word
        elif current_count >= max_count -4:
            max_count5 = current_count
            max_word5 = current_word        
            # write result to STDOUT
            #print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
#if current_count > max_count:
    #max_count= current_count 
    #max_word = current_word

print ('%s\t%s' % (max_word, max_count))
print ('%s\t%s' % (max_word2, max_count2))
print ('%s\t%s' % (max_word3, max_count3))
print ('%s\t%s' % (max_word4, max_count4))
print ('%s\t%s' % (max_word5, max_count5))