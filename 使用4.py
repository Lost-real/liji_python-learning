a=open("1.txt","r")
b=open("2.txt","r",encoding="utf-8")
c={}
d={}
for i in a:
    i1=i.strip().split()
    c[i[0]]=1
for m in b:
    m=m.strip().split()
    d[m[0]]=m[1]
for i in c.keys():
    if i in d.keys():
        print("y")
    else:
        print("n")