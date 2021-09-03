#!./hadoop-env/bin/python
# -- coding: utf-8 --
import sys
import re

title_vineta = '<TITLE>'
title_vineta_final = '</TITLE>'

#regex_body = '/\'/.*<BODY><\\\\\\\\BODY>$/m\'/m'
#regex_title = '/\'/.*<TITLE><\\\\\\\\TITLE>$/m\'/m'
for line in sys.stdin:
    text_title = line[line.find('<TITLE>'):line.find('</TITLE>')].replace('</TITLE>','').replace('<TITLE>','')
      # remove leading and trailing whitespace
    line = text_title.strip()
      # split the line into words
    words = line.split()
      #words_title = words.replace('<TITLE>    ','').split(',')[0]
    for word in words:
        word_body = re.sub('[^a-zA-Z0-9 \n\.]','', word)
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

