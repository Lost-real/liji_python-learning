n = 0
with open("zzztotgen31spAT5G67590.1.txt","r") as fn1:
    for i in fn1:
        eachline = i.strip()
        # print(eachline)
        n = n + 1
        if eachline.startswith(">"):
            print(eachline)
        else:
            if n ==2:
                newlist = ["1" for i in eachline]
                print("".join(newlist))
                dz = eachline
                # print(dz)
            else:
                newlist = []
                for i,j in zip(eachline,dz):
                    if i==j:
                        newlist.append("1")
                    else:
                        newlist.append("0")
                print("".join(newlist))



