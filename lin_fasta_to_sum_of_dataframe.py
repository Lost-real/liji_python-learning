def function01(a):
    n = 0
    newlist = []  # 创建一个列表
    for i in a:
        eachline = i.strip()
        n = n + 1
        if eachline.startswith(">"):#把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
            # eachline = eachline.strip().split('>')[1]
            #
            # newlist.append("\n"+eachline)
            # newlist.append(eachline)
            continue
        else:
            if n ==2:
                # print(eachline)
                for i in eachline:
                    i = i.strip("\n").split()
                    i = "".join(i)
                    if i == "A":
                        newlist.append("1")
                    elif i == "T":
                        newlist.append("1")
                    elif i == "C":
                        newlist.append("1")
                    elif i == "G":
                        newlist.append("1")
                    elif i == "X":
                        newlist.append("1")
                    else:
                        newlist.append("0")
                    # print("".join(newlist))
                    # newlist = ["1" for i in eachline]
                # b.write("".join(newlist)+"\n")
                dz = eachline
            else:
                for i,j in zip(eachline,dz):
                    if i==j and i!="-":
                        newlist.append("1")
                    else:
                        newlist.append("0")
    return (" ".join(newlist))

def sum_of_dataframe(a):
    list01 = []
    n = 0
    for i in a:
        if i != "0" and i != "1":
            continue
            # list01.append(i)
        else:
            # continue
            list01.append(i)
    # print(list01)
    for i in list01:
        n += int(i)
    print(n)
import argparse
parser = argparse.ArgumentParser(description="矩阵：10行100列，第一列是列名字,想计算每一列的和,输出格式：文本名字+每一列的和")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open (args.file1,"r") as f1:
    a4=function01(f1)
    sum_of_dataframe(a4)