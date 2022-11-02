#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open(args.file1,"r") as fn1:
    newlist = []#创建一个列表
    n=0
    for i in fn1:
        eachline = i.strip()
        n = n + 1
        if eachline.startswith(">"):  # 把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
            print(eachline)
            # b.write(eachline+"\n")
        else:
            if n == 2:
                # print(eachline)
                for i in eachline:
                    i = i.strip("\n").split()
                    i = "".join(i)
                    if i in "ATGC":
                        newlist.append(i)
                print("".join(newlist))
                # b.write("".join(newlist)+"\n")
                dz = eachline
            else:
                newlist1 = []
                for i,j in zip(eachline,dz):
                    if j != "-":
                        newlist1.append(i)
                print("".join(newlist1))