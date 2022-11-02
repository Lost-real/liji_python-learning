import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open(args.file1,"r") as f1:
    for i in f1:
        i = i.strip()
        b = int(len(i) / 2)
        # i=i.split()
        # print(b)
        # for j in i:
        #     print(j[1])
        for m in range(b):
            print(i[m] + ":" + i[b-m])