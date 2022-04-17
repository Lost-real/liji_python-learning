#! /usr/bin/env python
#usage: python hash-always.py -f1 1.list -f2 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f2","--file2",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f1","--file1",help="the list by which you want to extract from the file")
args = parser.parse_args()

hasha = {}

with open(args.file1,"r") as fn1:
    for i in fn1:
        line = i.strip()
        hasha[line] = 1

with open(args.file2,"r") as fn2:
    for i in fn2:
        eachline = i.strip()
        colist = eachline.split("\t")
        if colist[0] in hasha.keys():
            print(eachline)         
