a=open("31.txt","r")
def convert(b):
    n = 0
    newlist = []  # 创建一个列表
    for i in b:
        eachline = i.strip()
        n = n + 1
        if eachline.startswith(">"):#把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
            eachline = eachline.strip().split('>')[1]
            # print(eachline)
            # return (newlist.append(eachline))
            newlist.append("\n"+eachline)
            # newlist.append("\n")
            # b.write(eachline+"\n")
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
                    else:
                        newlist.append("0")
                # print("\t".join(newlist))

                # list01=["\t".join(i) for i in newlist]
                    # newlist = ["1" for i in eachline]
                # print("\t".join(newlist))
                # return ("\t".join(newlist))
                # "\t".join(newlist)
                # b.write("".join(newlist)+"\n")
                dz = eachline
            else:
                # newlist1 = []
                for i,j in zip(eachline,dz):
                    if i==j and i!="-":
                        newlist.append("1")
                    else:
                        newlist.append("0")
                # print(newlist)
                # print("\t".join(newlist1))
            #     print("\t".join(newlist1))
            #     list01=["\t".join(i) for i in newlist1]
    # print("\t".join(newlist))
    return ("\t".join(newlist))
# print(newlist1)
c=convert(a)
print(c)
