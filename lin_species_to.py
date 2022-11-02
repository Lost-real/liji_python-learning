import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
n = 0
newlist = []#创建一个列表
# b=open(".txt","w")
with open(args.file1,"r") as fn1:
    for i in fn1:
        j=i.strip().split()
        f = open(j[0]+".txt",'w')
        # print("\n".join(j))
        # for j in i:
        #     print("".join(j))
        # print(i)
        f.write("\n".join(j))