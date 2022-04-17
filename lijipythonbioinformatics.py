# DNAseq="ATCGTTGC"
# mRNAseq=DNAseq.replace("T","U")
# print(mRNAseq)
# c=DNAseq.count("C")
# print(c)
# g=DNAseq.count("G")
# print(g)
# p=mRNAseq.find("AUG")
# print(p)
#注意字符串中有split()这个方法，并且，split可以把字符串变成list
# m="This string has words separated by spaces".split()
# print(m)
# n= "Alex Doe,5555-2333,nobody@example.com".split(",")
# print(n)
# l=";".join([’Alex Doe’, ’5555-2333’, ’nobody@example.com’])
# l=['A','C','G','T']
# l1="".join(['A','C','G','T'])
# print(l1)
# for i in l:
#     l1= ''.join(l)
#     print(l1)

# A = [0,1,2,3,4,5]
# a=[3*x for x in A]
# print(a)

#筛选列表中含有某种特殊字符串
# B=['aaa','baa','cdd']
# C=[b.strip() for b in B if 'a' in b]
# print(C)
#######################################################
#注意list可以把一串字符串变成单个字符串，而"".join()可以把单个字符串变成一串字符串
# aseq="atgcaattccc"
# a=list(aseq)
# # print(a)
# b=str(a)
# print(b)
# c="".join(a)
# print(c)

#########################
# import copy
# a=[1,2,3]
# print(a)
# a1=a.pop()
# print(a1)
# b1=a[:]
# b=copy.copy(a)
# print(b)
# print(b1)
# a1=a.append(9)
# print(a1)
##########################

# a=[1,2,3]
#一定要注意列表a使用append增加元素时，不能用a1=a.append(9),只能使用a.append(9),如下所示：
#a1=a.append(9)#这样写法是错误的
# a.append(9)
# print(a)
# a.extend([4,5,6])
# print(a)#注意，这样写是错误的print(a.extend[4,5,6])
##################################################
#打印出列表seqdata中，第一个元素"MRVLLLVVAA"中，第3个元素
# seqdata=["MRVLLLVVAA",12,"0EHFJL874"]
# print(seqdata[0][2])
###########################################################
#字典
# IUPAC={"A":"Ala","C":"Cys","E":"Glu"}
# for i in IUPAC:
#     print(i)
# print(IUPAC.keys())#打印出字典的键
# a=IUPAC.items()
# print(a)
# b=IUPAC.get("A","No")
# print(b)
###########################################
# protseq = input("Protein sequence: ").upper()
# protdeg = {"A":4,"C":2,"D":2,"E":2,"F":2,"G":4,"H":2,
# "I":3,"K":2,"L":6,"M":1,"N":2,"P":4,"Q":2,
# "R":6,"S":6,"T":4,"V":4,"W":1,"Y":2}
# segsvalues = []
# for aa in range(len(protseq)):
#     segment = protseq[aa:aa+15]
#     degen = 0
#     if len(segment)==15:
#         for x in segment:
#             degen += protdeg.get(x,3.05)
#         segsvalues.append(degen)
#     else:
#         pass
# min_value = min(segsvalues)
# minpos = segsvalues.index(min_value)
# print(protseq[minpos:minpos+15])
##########################################################
# a=str(12345678998765432123456789)
# # dict={}
# a1=[i for i in range(len(a))]
# a2=[i for i in a]
# a3=dict(zip(a1,a2))
# print(a3)
# b=[]
# for i in range(len(a)):
#     c=a[i:i+5]
#     # print(c)
#     d=0
#     if len(c)==5:
#         for j in c:
#             d+=int(j)
#             b.append(d)
#     else:
#         pass
# max_value=max(b)
# max_pos=b.index(max_value)
# print(max_pos)

##########################################################################
# a=str(12345678998765432123456789)
# # dict={}
# a1=[i for i in range(len(a))]
# a2=[i for i in a]
# a3=dict(zip(a1,a2))
# # print(a3)
# b=[]
# for i in range(len(a)):
#     c=a1[i:i+5]
#     # print(c)
#     d=0
#     if len(c)==5:
#         for j in c:
#             d+=int(a3.get(j,100))
#         b.append(d)
#     else:
#         pass
# print(b)
# max_value=max(b)
# max_pos=b.index(max_value)
# print(a[max_pos:max_pos+5])
###########################################################################
# def protcharge(AAseq):
#     '''Returns the net charge of a protein sequence'''
#     protseq=AAseq.upper()
#     charge=-0.002
#     AACharge={"C":-0.045,"D":-0.999,"E":-0.998,"H":0.091,"K":1,"R":1,"Y":-0.001}
#     for aa in protseq:
#         charge+=AACharge.get(aa,0)
#     return charge
# a=protcharge("CED")
# print(a)
############################################################################################
# def chargeandprop(AAseq):
#     ''' Returns the net charge of a protein sequence and proportion of charged amino acids'''
#     protseq=AAseq.upper()
#     charge=-0.002
#     cp=0
#     AACharge={"C":-.045,"D":-.999,"E":-.998,"H":.091,"K":1,"R":1,"Y":-.001}
#     for aa in protseq:
#         charge+=AACharge.get(aa,0)
#         if aa in AACharge:
#             cp +=1
#     prop=100.*cp/len(AAseq)
#     return (charge,prop)
# a= chargeandprop("QTALLVVLVLLAVALQATEAGPYGA")
# print(a)
#########################################################################
# def savelist(L,fname):
#     ''' A list (L) is saved in a file (fname) '''
#     fh=open(fname,"w")
#     for x in L:
#         fh.write('%s'%x)
#     fh.close()
#     return None
# a=savelist([1,2,3],'x.txt')
# print(a)
###############################################################
# def test(x):
#     global z
#     z=10
#     print("z=%s"%z)
#     return x*2
# z=1
# print(test(4))
#########################################
class Square:
    def __init__(self):
        self.side=1

bob=Square()
print(bob.side)
