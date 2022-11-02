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
        # i=i.strip()
        # print(i)
        if i.startswith(">"):
            name = i.strip().split('>')[1]
            # i=i.replace(">","")
            # print(i)
            seq[name] = ""
        else:
            seq[name] += i.replace("\n", "")
    for i in seq.keys():
        if seq[i] != "":
            print(i + " "*10 + seq[i])
