#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
-Extract the year and print it
-Extract the names and rank numbers and just print them
-Get the names data into a dict and print it
-Build the [year, 'name rank', ... ] list and print it
-Fix main() to use the extract_names list
"""

def extract_names(filename):
  fp=open(filename,'rU')
  txt=fp.read()
  l=[]
  y=re.search(r'Popularity\sin\s(\d\d\d\d)',txt)
  if not y:
   print 'not find the year\n'
  y1=y.group(1)
  l.append(y1)
  
  n= {}
  r = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', txt)
  for e in r:
    (rank,boyname,girlname) = e
    if boyname not in n:
      n[boyname] = rank
    if girlname not in n:
      n[girlname] = rank
    
  sort = sorted(n.keys())
  for name in sort:
    nl.append(name + " " + n[name])
  return nl
  
 


def main():
  args = sys.argv[1:]
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

 
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  
if __name__ == '__main__':
  main()
