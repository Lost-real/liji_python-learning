a=open("plusminusmerge.txt","r")
b=open("plusminusmergeplusout.txt","w")
for i in a:
    i=i.strip().split("\t")
    # print(i[0])
    b.write("nohup bedtools getfasta -fi "+str(i[0])+ " -bed " +str(i[1])+" -fo "+str(i[1])+"promoter -name & \n")
    # i=" ".join(i)
    # print(i)