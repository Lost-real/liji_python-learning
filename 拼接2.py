a=open("cat_minus_plus.txt","r")
b=open("cat_minus_plusout.txt","w")
for i in a:
    line=i.strip().split()
    b.write("nohup cat "+str(line[0])+" "+str(line[1])+" > "+str(line[2]) + " & \n")


# a=open("genomeout.txt","r")
# b=open("genomeout2.txt","w")
# for i in a:
#     line=i.strip()
#     b.write("nohup cat "+str(line)+" | cut -d . -f1 > " +str(line)+"in & \n")

a=open("pathminuspromoter.txt","r")
b=open("pathminuspromoterout.txt","w")
for i in a:
    i=i.strip()
    # b.write("nohup cat "+str(i)+" | awk -v OFS='<' '{print $2,$1}'> "+str(i)+"4 & \n")
    b.write("nohup python Reversecomplement1.py -f1 "+str(i)+" > "+str(i) +"Reverse & \n" )