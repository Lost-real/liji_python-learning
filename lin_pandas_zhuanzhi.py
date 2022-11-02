#python lin_reverse_column.py -f1 At5utr200bpmerge1sortedreplacefillup > At5utr200bpmerge1sortedreplacefillupreverse
import pandas as pd
import argparse
parser = argparse.ArgumentParser(description="假如有1行，10列，分别是a 1 2 3 4 5 6 7 8 9, 目的是输出a 9 8 7 6 5 4 3 2 1 ")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
df=pd.read_csv("args.file1")
df1=df.T
# print(df.T)
print(df1.to_csv("At5utr200bpmerge1sortedreplacefillupreversezhuanzhi.csv",header=None))