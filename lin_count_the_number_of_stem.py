#用于计算多个同源序列的保守性
import pandas as pd
import argparse
parser = argparse.ArgumentParser(description="比如：矩阵有10行100列,第一列是列名,我们想计算整个矩阵的平均值；输出格式：文本名字+整个矩阵的平均值")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()

with open (args.file1,"r") as f1:
    n = 0
    for i in f1:
        i = i.strip()
        if i.startswith("S"):
            n += 1
        else:
            continue
print (args.file1,n)
