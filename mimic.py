#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import random
import sys
import re

def mimic_dict(filename):
  fp=open(filename,'r')
  txt=fp.read()
  fp.close()
  w=txt.split()
  mimic_dict={}
  s=''
  for e in w:
    if not s in mimic_dict:
     mimic_dict[s] = [e]
    else:
     mimic_dict[s].append(e)
     s = e
  return mimic_dict
  
  
def print_mimic(mimic_dict,e):
  for i in range(200):
    print e,
    j = mimic_dict.get(e)
    if not j:
      j = l[' ']
    word = random.choice(j)


def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
