import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    c=[]
    for i in f1:
        i=i.split()
        # b=int(len(i))
        c=i[0:1]+i[int(len(i)-517):len(i)]
        print("\t".join(c))
