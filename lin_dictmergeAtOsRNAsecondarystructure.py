import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f2","--file2",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
d1={}
d2={}
with open(args.file1,"r") as f1:
    for i in f1:
        i = i.strip().split()
        d1[i[0]] = i[1:3]
    # print(dict)
with open(args.file2, "r") as f2:
    for j in f2:
        j = j.strip().split()
        d2[j[0]] = 1
for m in d2.keys():
    if m in d1.keys():
        print("\n".join(d1[m]))
