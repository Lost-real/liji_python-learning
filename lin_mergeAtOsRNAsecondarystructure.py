import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
def merge(m,n):
    m2=[]
    n2=[]
    with open(m,"r") as m1:
        for i in m1:
            i=i.strip().split()
            m2.append(i)
    with open(n,"r") as n1:
        for j in n1:
            j=j.strip().split()
            n2.append(j)
            # print("".join(i)+"".join(j)+"\n")
    for i,j in zip(m2,n2):
        print("".join(i),"".join(j))

with open(args.file1,"r") as f1:
    for i in f1:
        i=i.strip().split()
        m=i[0]
        n=i[1]
        # print(m)
        merge(m,n)