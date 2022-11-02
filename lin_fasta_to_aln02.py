#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open(args.file1,"r") as fn1:
    seq = {}
    print("CLUSTAL" + "\n")
    for i in fn1:
        i=i.strip().split()
        print(str(i[0])+" "*10+"".join(i[1:]))
