#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f2","--file2",help="the list by which you want to extract from the file")
args = parser.parse_args()

c={}
d={}

with open(args.file1,"r") as fn1:
	for i in fn1:
		i=i.strip().split()
		c[i[0]]=1

with open(args.file2,"r") as fn2:
	for m in fn2:
    		m=m.strip().split()
   	 	d[m[0]]=m[1]
for i in c.keys():
    if i in d.keys():
        print(d[i])
    else:
        print("n")
