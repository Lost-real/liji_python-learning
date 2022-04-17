n = 0
newlist = []
b=open("out1.sequence.txt","w")
with open("out.zzztotgen31spAT5G67590.1","r") as fn1:
    for i in fn1:
        eachline = i.strip()
        n = n + 1
        if eachline.startswith(">"):
            print(eachline)
            b.write(eachline+"\n")
        else:
            if n ==2:
                # print(eachline)
                for i in eachline:
                    i = i.strip("\n").split()
                    i = "".join(i)
                    if i == "a":
                        newlist.append("1")
                    elif i == "t":
                        newlist.append("1")
                    elif i == "c":
                        newlist.append("1")
                    elif i == "g":
                        newlist.append("1")
                    else:
                        newlist.append("0")
                    # print("".join(newlist))
                    # newlist = ["1" for i in eachline]
                print("".join(newlist))
                b.write("".join(newlist)+"\n")
                dz = eachline
            else:
                newlist = []
                for i,j in zip(eachline,dz):
                    if i==j:
                        newlist.append("1")
                    else:
                        newlist.append("0")
                print("".join(newlist))
                b.write("".join(newlist)+"\n")

# n = 0
# newlist = []
# c=open("out2.sequence.txt","w")
# with open("out1.sequence.txt","r") as fn1:
#     for i in fn1:
#         eachline = i.strip()
#         n = n + 1
#         if eachline.startswith(">"):
#             print(eachline)
#             c.write(eachline+"\n")
#         else:
#             if n ==2:
#                 # print(eachline)
#                 print(eachline)
#                 c.write(eachline+"\n")
#
#                 # print("".join(newlist))
#                 dz=eachline
#             else:
#                 newlist = []
#                 for i, j in zip(eachline, dz):
#                     if i == j and j== "1":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#                 print("".join(newlist))
#                 c.write("".join(newlist)+"\n")



