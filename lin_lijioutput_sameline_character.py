import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

with open (args.file1,"r") as f1:
    list01=[]
    n=0

    for i in f1:
        i=i.strip()
        list01.append(i)
        lenth=len(list01[0])
    while n<=1:
        print(list01[n][0:lenth])
        n=n+1
