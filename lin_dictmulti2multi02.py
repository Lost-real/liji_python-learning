#python lin_dictmulti2multi02.py -f1 rice_arabidopsis-3.txt -f2 Atonly9071.txt > outputAtonly9071.txt
#python lin_dictmulti2multi02.py -f1 rice_arabidopsis-3.txt -f2 Osonly5133.txt > outputOsonly5133.txt
import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="多对多的文件")
parser.add_argument("-f2","--file2",help="文件只有一列")
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
        if j[0] in c.keys():
            print(" ".join(c[j[0]]))
        else:
            continue
