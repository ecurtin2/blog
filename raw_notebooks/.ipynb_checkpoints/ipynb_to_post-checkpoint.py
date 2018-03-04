import os
import sys

site_basedir = ".."
fname = sys.argv[1]
title = raw_input("Enter the desired title: ")

fname, extension = os.path.splitext(fname)
if not (extension == ".ipynb"):
    print "Error: File must be .ipynb format."
    sys.exit()

img_dir = "/images/" + fname 
os.system("jupyter nbconvert --to Markdown " + fname + extension)

with open(fname + ".md", "r") as f:
    lines = f.readlines()
    newtext = '<img class="post-image" src="' + img_dir
    lines = [line.replace(fname + "_files", newtext).replace(')','">').replace('![png](','') 
            if (fname + "_files" in line) else line for line in lines]

lines.insert(0, "---")
lines.insert(0, "title: " + title)
lines.insert(0, "layout: post")
lines.insert(0, "---")

with open(fname + ".md", "w") as f:
    f.write('\n'.join(lines) + '\n')

os.system("mv " + fname + ".md " + site_basedir + "/_posts/")
os.system("mkdir " + site_basedir + img_dir)
os.system("mv " + fname + "_files/* " + site_basedir + img_dir)
os.system("rmdir " + fname + "_files")  
