import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open(args.file1,"r") as f1:
    a1=f1.readlines()
with open(args.file2,"r") as f2:
    b1=f1.readlines()

c=a1+b1
print("\n".join(c))