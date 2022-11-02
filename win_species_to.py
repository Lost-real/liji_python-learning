n = 0
newlist = []#创建一个列表
# b=open(".txt","w")
with open("001.txt","r") as fn1:
    for i in fn1:
        j=i.strip().split()
        f = open(j[0]+".txt",'w')
        # print("\n".join(j))
        # for j in i:
        #     print("".join(j))
        # print(i)
        f.write("\n".join(j))