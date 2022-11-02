# list1 =[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9,7,6]
# # print(list1)
# a1 = [i for i in range(len(list1))]
# # print(a1)
# a2 = [i for i in list1]
# a3 = dict(zip(a1, a2))
# # print(a3)
# b = []
# n=5
# while n<=9:
#     for i in range(len(list1)):
#         c = list1[i:i + n]
#         # print(c)
#         d = 0
#         if len(c) == n:
#             for j in c:
#                 d += int(a3.get(j, 100))
#             b.append(d)
#         else:
#             pass
#     n+=1
# # print(b)


########################################################################################

# chl_fasta = {}
#
# with open ("1229001.txt","r") as fn2:
#     for row in fn2:
#         if ">" in row:
#             fsy = row.split()
#             chl_gene = fsy[0].replace('>','')
#             fsy_sequence =''
#         else:
#             ro=row.strip()
#             # print(ro)
#             sequences = ro.split()
#             # print(row)
#             # print(sequences)
#             store = sequences[0]
#             # print(sequences[0])
#             fsy_sequence = fsy_sequence+store
#             chl_fasta[chl_gene] = fsy_sequence
# print(chl_fasta)
##########################################################################################
# with open("ztotgen31spAT1G01550.2.txt","r") as fr:
# # fr=open('ztotgen31spAT1G01550.2.txt', 'r')
#     fw=open('ztotgen31spAT1G01550.2-11.txt', 'w')
#     seq={}
#     for line in fr:
#         if line.startswith('>'):    #判断字符串是否以‘>开始’
#             name=line.split()[0]    #以空格为分隔符，并取序列号为0的项。
#             seq[name]=''
#         else:
#             seq[name]+=line.replace('\n', '')
#
# for i in seq.keys():
#     fw.write(i+"\n")
#     # fw.write('\n')
#     fw.write(seq[i]+"\n")
#     # fw.write('\n')
# fr.close()
#
# n = 0
# newlist = []#创建一个列表
# b=open("ztotgen31spAT1G01550.2-1-5.txt","w")
# with open("ztotgen31spAT1G01550.2-11.txt","r") as fn1:
#     for i in fn1:
#         eachline = i.strip()
#         n = n + 1
#         if eachline.startswith(">"):#把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
#             print(eachline)
#             b.write(eachline+"\n")
#         else:
#             if n ==2:
#                 # print("\t".join(eachline))
#
#                 for i in eachline:
#                     i = i.strip()
#                     # print(i)
#                     # print("".join(i))
#                     i = "".join(i)
#
#                     if i == "a":
#                         newlist.append("1")
#                     elif i == "t":
#                         newlist.append("1")
#                     elif i == "c":
#                         newlist.append("1")
#                     elif i == "g":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#                     # print("".join(newlist))
#                     # newlist = ["1" for i in eachline]
#                 print("\t".join(newlist))
#                 b.write("\t".join(newlist)+"\n")
#                 dz = eachline
#             else:
#                 newlist = []
#                 for i,j in zip(eachline,dz):
#                     if i==j and i!="-":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#                 print("\t".join(newlist))
#                 b.write("\t".join(newlist)+"\n")
#######################################################################################
n=0
with open("AT4G28200.1.txt","r") as fr:
    for i in fr:
        eachline=i.strip()
        if eachline.startswith(">"):
            n=n+1
        else:
            continue
print(n)

