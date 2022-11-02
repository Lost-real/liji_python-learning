#python lin_dictmulti2multi.py -f1 rice_arabidopsis-3.txt -f2 Os_At7828.txt > outputOs_At7828.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="多对多的文件")
parser.add_argument("-f2","--file2",help="文件只有两列")
args = parser.parse_args()
c={}
with open(args.file1,"r") as f1:

    for i in f1:
        i = i.strip().split()
        # print(i)
        for j in range(74):
            c[i[j]] = i[:]

with open(args.file2, "r") as f2:
    for j in f2:
        j = j.strip().split()
        if j[0] in c.keys() and j[1] in c[j[0]]:
            print(j[0],"yes")
        else:
            print(j[0],"no")
