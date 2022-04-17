#! /usr/bin/env python
#usage: python hash-always.py -l 1.list -f 2.txt > out.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

d = []
chl_fasta = {}
with open (args.file1,"r") as fn1:
    for row in fn1:
        if ">" in row:
            fsy = row.split()
            chl_gene = fsy[0].replace('>', '')
            fsy_sequence = ''
        else:
            ro=row.strip()
            # print(ro)
            sequences = ro.split()
            # print(row)
            # print(sequences)
            store = sequences[0]
            # print(sequences[0])
            fsy_sequence = str(fsy_sequence) + str(store)
            chl_fasta[chl_gene] = fsy_sequence
def reverse_complement(seq):
  ntComplement = {'A':'T','T':'A','G':'C','C':'G','Y':'R','R':'Y','K':'M','M':'K','H':'D','D':'H','S':'W','W':'S','B':'V','V':'B','N':'N','a':'t','t':'a','c':'g','g':'c','n':'n','r':'y','y':'r'}
  RevSeqList = list(reversed(seq))
  RevComSeqList = [ntComplement[k] for k in RevSeqList]
  RevComSeq = ''.join(RevComSeqList)
  return RevComSeq
for i in chl_fasta:
    h=reverse_complement(chl_fasta[i])
    result=">"+str(i)+"\n"+str(h)
    print(result)
