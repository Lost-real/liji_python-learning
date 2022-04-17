import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f2","--file2",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f1","--file1",help="the list by which you want to extract from the file")
args = parser.parse_args()
d={}
with open(args.file2,"r") as fn2:
    for i in fn2:
        i=i.strip().split()
        d[i[0]]=i[:]
with open(args.file1,"r") as fn1:
    for j in fn1:
        j=j.strip().split()
        if j[0] in d.keys():
            print("\t".join(d[j[0]]))