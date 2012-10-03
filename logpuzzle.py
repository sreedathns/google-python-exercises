#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class


import os
import re
import sys
import urllib

def sort_key(url):
  m = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if m:
    return m.group(2)
  else:
    return url

def read_urls(filename):
  ub = filename.index('_')
  h = filename[ub + 1:]
  l = {}
  f = open(filename)
  for line in f:
    m = re.search(r'"GET (\S+)', line)
    if m:
      p= m.group(1)
      if 'puzzle' in p:
        l['http://' + h + p] = 1
  return sorted(l.keys(), key=sort_key)

def download_images(img_urls, dest_dir):
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')
  i = 0
  for img_url in img_urls:
    l_name = 'img%d' % i
    print 'downloading...', img_url
    urllib.urlretrieve(img_url, os.path.join(dest_dir, local_name))
    index.write('<img src="%s">' % (l_name,))
    i += 1
  index.write('\n</body></html>\n')
  index.close()
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
