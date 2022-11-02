a=open("1.txt","r")
b=open("2.txt","r",encoding="utf-8")
c={}
d={}
e=open("3.txt","w")
for i in a:
    i1=i.strip().split()
    # print(i1)
    c[i[0]]=1
# print(c)
for m in b:
    m=m.strip().split()
    d[m[0]]=m[1]
# print(d)
for i in c.keys():
#
    if i in d.keys():
        e.write("y \n")
    else:
        e.write("n \n")
# print(str(c))

