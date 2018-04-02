#!/usr/bin/env python3

import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Strip header and footer from input html and optionally add style.')
parser.add_argument('html', type=str, help='An html file to process')
parser.add_argument('-c', action='store', dest='css', type=str, help='A css file to inject into output html')
parser.add_argument('-o', action='store', dest='out', type=str, help='Output filename')

opts = vars(parser.parse_args())

htmlfile = opts['html']
cssfile = opts['css']
outfile = opts['out']


with open(htmlfile, 'r') as f:
    s = f.read()
    
bs = BeautifulSoup(s, 'lxml')

for h in bs.find_all('header'):
    h.decompose()
for f in bs.find_all('footer'):
    f.decompose()
    
if cssfile is not None:
    with open(cssfile, 'r') as css:
        style = css.read()
else:
    style = ''
    
style = '<style>\n' + style + '\n</style>\n'

outlist = str(bs).split('\n')
    
for i, line in enumerate(outlist):
    if 'stylesheet' in line:
        break
        
outlist = outlist[:i] + [style] + outlist[i:]
outstr = '\n'.join(outlist)

with open(outfile, 'w') as out:
    out.write(outstr)
