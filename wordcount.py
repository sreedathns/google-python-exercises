#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
def wordcount(filename):
  wc = {}
  fp = open(filename, 'r')
  for line in fp:
   words=line.split()
   for e in words:
       e = e.lower()
       if not e in wc:
         wc[e] = 1
       else:
         wc[e] = wc[e] + 1
   return wc


def print_words(filename):
  wc = wordcount(filename)
  words = sorted(wc.keys())
  for e in words:
    print e, wc[e]

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
