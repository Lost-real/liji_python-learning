a=open("list1.txt",'r')
# b=open("list2.txt","w")
for i in a:
    i=i.strip().split()
    # i=i.strip("\n")
    # print(i[0:22])
    print(i)
    # print(type(i))
    # c="".join(i)
    # print(c)
    # print(type(c))
    # b[i[1]]=i[2]+","+i[0]
    # b.write(i[1]+" "+i[3]+'\n')
