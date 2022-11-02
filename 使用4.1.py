#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

d = []
chl_fasta = {}

a=with open("sequence.txt","r") as f1:
# # print(type(a))
# b=a.strip().split()
# c="".join(reversed(b))
    for row in f1:
        if ">" in row:
            fsy = row.split()
            chl_gene = fsy[0].replace('>', '')
            fsy_sequence = ''
        else:
            ro=row.strip()
            sequences = ro.split()
            store = sequences[0]
            fsy_sequence = fsy_sequence + store
            chl_fasta[chl_gene] = fsy_sequence
    # def reverse(seq):
    #     for i in seq:
    #         m=''.join(reversed(i))
    #         for i in m:
    #             if i =="A":
    #                 d.append("U")
    #             elif i =="T":
    #                 # i=="A"
    #                 d.append("A")
    #             elif i=="C":
    #                 d.append("G")
    #             else:
    #                 d.append("C")
    #             e="".join(d)
    #         print(e)
    #     return e
    # for i in chl_fasta:
    #     h=reverse(chl_fasta[i])
    #     print(h)
        # n=">"+str(i)+"\n"+str(h)
        # print(n)
for g in chl_fasta:
    m=''.join(reversed(chl_fasta[g]))
    for i in m:
        if i =="A":
            d.append("U")
        elif i =="T":
            # i=="A"
            d.append("A")
        elif i=="C":
            d.append("G")
        else:
            d.append("C")
    e="".join(d)
    j=">"+str(g)+"\n"+str(e)
print(j)