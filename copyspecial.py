#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

def get_path(dirname):
   l = []
   paths = os.listdir(dirname)
   for fname in paths:
     match = re.search(r'__(\w+)__', fname)
     if match:
       l.append(os.path.abspath(os.path.join(dirname, fname)))
  return l

def cpy(paths,dirname):
if not os.path.exists(dirname):
   os.mkdir(dirname)
   for path in paths:
     fname = os.path.basename(path)
      shutil.copy(path, os.path.join(to_dir, fname))

def tzip(path,zfile):
a='zip -j '+zfile+' '+' '.join(path)
print "Command I'm going to do:" + a
(status,output)=commands.getstatusoutput(a)
if status:
sys.stderr.write(output)
sys.exit(1)


def main():
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
    
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
 
  paths = []
  for dirname in args:
    paths.extend(get_path(dirname))

  if todir:
    cpy(paths, todir)
  elif tozip:
    zipto(paths, tozip)
  else:
    print '\n'.join(paths)
    
if __name__ == "__main__":
  main()
