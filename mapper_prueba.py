#!/usr/bin/env python
"""mapper.py"""

import sys
title_vineta = '<TITLE>'
title_vineta_final = '</TITLE>'
# input comes from STDIN (standard input)
for line in sys.stdin:
    if title_vineta in line:
    # remove leading and trailing whitespace
        line = line.strip()
    # split the line into words
        words = line.split()
    # increase counters
        for word in words:
            if title_vineta in word:
                word = word.replace(title_vineta,'')
            if title_vineta_final in word:
                word = word.replace(title_vineta_final,'')
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
            print ('%s\t%s' % (word.lower(), 1))