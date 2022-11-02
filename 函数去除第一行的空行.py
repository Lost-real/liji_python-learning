a=open("32.txt","r")
def remove_enter(a):
    # n=0
    list01=[]
    for i in a:
        if i.startswith("\n"):
        # i=i.strip()
        # if n==1:
            continue
        else:
            list01.append(i)
    return ("".join(list01))
c=remove_enter(a)
print(c)
