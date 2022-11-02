# a=open('homology_gene1.txt','r')
# b=open("homologygene138-388.txt ","r")
# c=open("outhomologygene138-388.txt","w")
# for i in b:
#     i=i.strip().split()
#     c.write('''nohup cat homology_gene138-388.txt | awk '{print $'''+ str(i[0])+ "}'"+"> "+str(i[1])+" & \n")


# b=open("1homologygene138-388.txt","r")
# c=open("out1homologygene138-388.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) +" -f2 the_1kb_promoter_of_homologous_gene > outhomology_"+str(i)+" & \n")

# b=open("pathgenegff3","r")
# c=open("outpathgenegff3.txt","w")
# for i in b:
#     i=i.strip()
    # c.write("nohup cat "+str(i) + ''' | grep "CDS" | awk '{print $1,$4,$5,$7,$9}' | cut -d "." -f1,2,3 | sed 's/ID=/ /' | awk -v OFS="1992" '{print $1,$2,$3,$5,$4}' | uniq -f 3 | awk '{ if ($5=="+") {print $1,$2-1000,$2,$4,$5}else {print $1,$3,$3+1000,$4,$5}}'> '''+str(i)+"123 & \n")

# b=open("pathgff4.txt","r")
# c=open("outpathgff4.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup cat "+str(i) +''' | awk '{if($2>=0){print $0}}' | awk -v OFS="12345678" '{print $1,$2,$3,$4,$5}' > '''+str(i)+"4567 & \n")

# b=open("pathgff5.txt","r")
# c=open("outpathgff5plus.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup cat "+str(i) +" | grep + >"+str(i)+"plus & \n")

# b=open("pathgff5.txt","r")
# c=open("outpathgff5plus.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup cat "+str(i) +" | grep + >"+str(i)+"plus & \n")

# b=open("minusreverse.txt","r")
# c=open("outminusreverse.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python ReverseComplementSequence.py -f1 "+str(i) + " > "+str(i)+"Reverse & \n")


# b=open("pathhomologygene1-137","r")
# c=open("outpathhomologygene1-137.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) + " -f2 the_1kb_promoter_of_homologous_gene > out"+str(i)+" & \n")

# b=open("pathAT138-388","r")
# c=open("outpathAT138-388.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) + " -f2 the_1kb_promoter_of_homologous_gene > out"+str(i)+" & \n")

# b=open("brassice1-500-1.txt","r")
# c=open("outbrassice1-500-1.txt","w")
# for i in b:
#     i=i.strip().split()
#     c.write('''nohup cat brassice1-500.txt | awk '{print $'''+ str(i[1])+ "}'"+"> "+str(i[0])+" & \n")

# b=open("pathbrassice_AT_1-500.txt","r")
# c=open("outpathbrassice_AT_1-500.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) +" -f2 the_1kb_promoter_of_homologous_gene > outbrassicaceae_"+str(i)+" & \n")

# b=open("brassice500-1000-1.txt","r")
# c=open("outbrassice500-1000-1.txt","w")
# for i in b:
#     i=i.strip().split()
#     c.write('''nohup cat brassice500-1000.txt | awk '{print $'''+ str(i[0])+ "}'"+"> "+str(i[1])+" & \n")

# b=open("pathbrassice_AT_501-1000.txt","r")
# c=open("outpathbrassice_AT_501-1000.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) +" -f2 the_1kb_promoter_of_homologous_gene > outbrassicaceae_"+str(i)+" & \n")

# b=open("brassicaceae20501-21000.txt","r")
# c=open("outbrassicaceae20501-21000.txt","w")
# for i in b:
#     i=i.strip().split()
#     c.write('''nohup cat 20501-21000.txt | awk '{print $'''+ str(i[0])+ "}'"+"> "+str(i[1])+" & \n")


# b=open("path20501-21000.txt","r")
# c=open("outpath20501-21000.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) +" -f2 the_1kb_promoter_of_homologous_gene > outbrassicaceae_"+str(i)+" & \n")

# b=open("brassic501-3000-1.txt","r")
# c=open("outbrassic501-3000-1.txt","w")
# for i in b:
#     i=i.strip().split()
#     c.write('''nohup cat brassic501-3000.txt | awk '{print $'''+ str(i[0])+ "}'"+"> "+str(i[1])+" & \n")

# b=open("pathATname501-3000","r")
# c=open("outpathATname501-3000","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0923.py -f1 "+str(i) +" -f2 the_1kb_promoter_of_homologous_gene > outbrassicaceae_"+str(i)+" & \n")

# b=open("ATname1-3000","r")
# c=open("outATname1-3000.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup python dict0925.py -f1 "+str(i) +" -f2 the_1kb_promoter_of_homologous_gene > outbrassicaceae_"+str(i)+" & \n")

# b=open("pathgenegff3","r")
# c=open("out3utrpathgenegff3.txt","w")
# for i in b:
#     i=i.strip()
#     c.write("nohup cat "+str(i) + ''' | grep "three" | awk '{print $1,$4,$5,$7,$9}' | cut -d "." -f1,2,3 | sed 's/ID=/ /' | awk -v OFS="\t" '{print $1,$2,$3,$5,$4}' | sort -k4,4 | uniq -f 3 | awk -v OFS="\t" '{ if ($5=="+") {print $1,$2-1,$2+999,$4,$5}else {print $1,$3-1001,$3-1,$4,$5}}' > '''+str(i)+"123 & \n")

b=open("path3UTRgff3.txt","r")
c=open("outpath3UTRgff3.txt","w")
for i in b:
    i=i.strip()
    c.write("nohup cat "+str(i) + ''' | grep "three" | awk '{print $1,$4,$5,$7,$9}' | cut -d ";" -f1 | sed 's/ID=/ /' > '''+str(i)+"4567 & \n")
