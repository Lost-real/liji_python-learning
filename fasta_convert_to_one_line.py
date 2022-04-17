#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
n = 0
newlist = []
with open(args.file1,"r") as fn1:
    for i in fn1:
        eachline = i.strip()
        n = n + 1
        if eachline.startswith(">"):
            print(eachline)
        else:
            if n ==2:
                # print(eachline)
                print(eachline)

                # print("".join(newlist))
                dz=eachline
            else:
                newlist = []
                for i, j in zip(eachline, dz):
                    if i == j and j== "1":
                        newlist.append("1")
                    else:
                        newlist.append("0")
                print("".join(newlist))