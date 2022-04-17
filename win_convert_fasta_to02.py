
n = 0
newlist = []
# c=open("out2.sequence.txt","w")
with open("outtest2.fasta","r") as fn1:
    for i in fn1:
        eachline = i.strip()
        n = n + 1
        if eachline.startswith(">"):
            print(eachline)
            # c.write(eachline+"\n")
        else:
            if n ==2:
                # print(eachline)
                print(eachline)
                # c.write(eachline+"\n")

                # print("".join(newlist))
                dz=eachline
            else:
                newlist = []
                for i, j in zip(eachline, dz):
                    if i == j and j== "1":
                        newlist.append("1")
                    else:
                        newlist.append("0")
                print("".join(newlist))
                # c.write("".join(newlist)+"\n")
