# n = 0
# newlist = []#创建一个列表
# # b=open(".txt","w")
# with open("001.txt","r") as fn1:
#     for i in fn1:
#         j=i.strip().split()
#         f = open(j[0]+".txt",'w')
#         # print("\n".join(j))
#         # for j in i:
#         #     print("".join(j))
#         # print(i)
#         f.write("\n".join(j))
#########################################################################
# '''
# 下面是生成乘法口诀的代码：如下所示
# 1*1=1
# 1*2=2 2*2=4
# '''
# i=0
#
# while i <9:
#     i+=1
#     for j in range(i):
#         j+=1
#         b=i*j
#         print("%d * %d = %d  "%(j,i,b),end=" ")
#     print("")

################################################
# a=["A","B","C","D"]
# b=["a","b","c","d"]
# dic={}
# for i in a:
#     for j in b:
#         dic{i}=j
#############################################
# a=">aaa"
# # a1=a.split()
# a2=a.replace('>', '')
# print(a2)
###################################################
# a="aaaaaaa"
# a1=a.strip().split()
# a2=a1[0]
# print(a2)

############################
#把svg图片格式转为pdf格式的代码
# -*- coding: utf-8 -*-

# 导入cairosvg库
# import cairosvg

# svg转pdf
# file_obj输入文件名 write_to输出文件名
# cairosvg.svg2pdf(file_obj=open("AT1G29780.1.svg", "rb"), write_to="output.pdf")

# svg转png
# file_obj输入文件名 write_to输出文件名 scale输出图像放大倍数
# cairosvg.svg2png(file_obj=open("AT1G29780.1.svg", "rb"), write_to="d:/output.png",scale=3.0)

############################################
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF
# svg_file = 'AT1G29780.1.svg'
# pdf_file = 'AT1G29780.1.pdf'
# drawing = svg2rlg(svg_file)
# renderPDF.drawToFile(drawing, pdf_file)
##########################################
#输出相同长度的字符串
#
# a=open("1.txt","r")
# list01=[]
# b=open("2.txt","a")
# n=0
#
# for i in a:
#     i=i.strip()
#     list01.append(i)
#     lenth=len(list01[0])
# while n<=1:
#     print(list01[n][0:lenth])
#     n=n+1
#############################################
# string="this string is"
# a=string.split()
# b=list(string)
# c=":".join(a)
# d=b.pop(0)
# print(a)
# print(b)
# print(c)
# print(d)
#####################################
# a=open("3.txt","r")
# b=0
# n=0
# for i in a:
#     i=i.strip()
#     # print(i[3])
#     while b<len(i):
#         if i[b]=="(":
#             n=n+1
#         b=b+1
# print(n/len(i))
        # else:
        #     continue

    # print(n)
    # print(len(i))
# list01=list(a)
# print(list01)
# a=open("Mmadata1")
# m=0
# m50=0
# m100=0
# m150=0
# m200=0
# m250=0
# m300=0
# m350=0
# m400=0
# m450=0
# m500=0
# for i in a:
#     i=i.strip()
#     i=int(i)
#     if i >500:
#         m500+=1
#     elif i>450:
#         m450+=1
#     elif i>400:
#         m400+=1
#     elif i>350:
#         m350+=1
#     elif i>300:
#         m300+=1
#     elif i>=250:
#         m250+=1
#     elif i>=200:
#         m200+=1
#     elif i>=150:
#         m150+=1
#     elif i>=100:
#         m100+=1
#     elif i>=50:
#         m50+=1
#     elif i >=0:
#         m+=1
# print(m,m50,m100,m150,m200,m250,m300,m350,m400,m450,m500)
#############################################################
# a=open("Mmadata1")
# m=0
# m50=0
# m100=0
# m150=0
# m200=0
# m250=0
# m300=0
# m350=0
# m400=0
# m450=0
# m500=0
# for i in a:
#     i=i.strip()
#     i=int(i)
#     if i >450:
#         m450+=1
#     elif i>=400:
#         m400+=1
#     elif i>350:
#         m350+=1
#     elif i>300:
#         m300+=1
#     elif i>250:
#         m250+=1
#     elif i>=200:
#         m200+=1
#     elif i>=150:
#         m150+=1
#     elif i>=100:
#         m100+=1
#     elif i>=50:
#         m50+=1
#     elif i >=0:
#         m+=1
# print(m,m50,m100,m150,m200,m250,m300,m350,m400,m450,m500)
################################################################
# string = 'daibahgk'
# li = list(string) # 将字符串转换为列表['d', 'a', 'i', 'b', 'a', 'h', 'g', 'k']
#
# # li.sort()     # 对列表里的字母进行排序,注意sort()没有返回值
# # print(li)
# # new_string = "".join(li)
# # print(new_string)
# # li.sort()     # 对列表里的字母进行排序,注意sort()没有返回值
#
# a=[str(i) for i in li]
# print(a)

##################################
# import pandas as pd
#
# from pandas.core.frame import DataFrame
# a=open("004.txt","r")
# b=open("006.txt","w")
# d=open("007.txt","w")
# c=[]
# for i in a:
#     i=i.strip()
#     # print(i)
#     # b.write(i+"\n")
#     i=i.split()
#     print(i[1:3])
#     c=i[0:1]+i[int(len(i)-3):len(i)]
#     # print(" ".join(c))
#     b.write(" ".join(c))
#     # d.write(" ".join(c)+"\n")
###############################################

# d={}
# with open ("013.txt","r") as fn2:
#     for row in fn2:
#         if ">" in row:
#             fsy = row.split()
#             chl_gene = fsy[0].replace('>', '')
#             fsy_sequence = ''
#             # print(chl_gene)
#
#         else:
#             ro=row.strip()
#             # print(ro)
#             sequences = ro.split()
#             # print(row)
#             # print(sequences)
#             store = sequences[0]
#             # print(sequences[0])
#             fsy_sequence = fsy_sequence + store
#             # print(fsy_sequence)
#             d[chl_gene] = fsy_sequence
#     print(d)
#     print(d['a'][0:3])#输出你想要的长度的value,amazing
# with open("011.txt","r") as fn2:
#     for i in fn2:
#         i=i.strip().split()
#         d[i[0]]=i[:]
#     print(d)
# with open("010.txt","r") as fn1:
#     for j in fn1:
#         j=j.strip().split()
#         if j[0] in d.keys():
#             print("\t".join(d[j[0]]))
#########################################################

# d = []
# chl_fasta = {}
# with open ("020.txt","r") as fn1:
#     for row in fn1:
#         if ">" in row:
#             fsy = row.split()
#             chl_gene = fsy[0].replace('>', '')
#             fsy_sequence = ''
#         else:
#             ro=row.strip()
#             # print(ro)
#             sequences = ro.split()
#             # print(row)
#             # print(sequences)
#             store = sequences[0]
#             # print(sequences[0])
#             fsy_sequence = str(fsy_sequence) + str(store)
#             chl_fasta[chl_gene] = fsy_sequence
# def reverse_complement(seq):
#   ntComplement = {'A':'T','T':'A','G':'C','C':'G','Y':'R','R':'Y','K':'M','M':'K','H':'D','D':'H','S':'W','W':'S','B':'V','V':'B','N':'N','a':'t','t':'a','c':'g','g':'c','n':'n','r':'y','y':'r'}
#   RevSeqList = list(reversed(seq))
#   RevComSeqList = [ntComplement[k] for k in RevSeqList]
#   RevComSeq = ''.join(RevComSeqList)
#   return RevComSeq
# for i in chl_fasta:
#     h=reverse_complement(chl_fasta[i])
#     result=">"+str(i)+"\n"+str(h)
#     print(result)

####################################
# seq="ATCG"
# ntComplement = {'A':'T','T':'A','G':'C','C':'G','Y':'R','R':'Y','K':'M','M':'K','H':'D','D':'H','S':'W','W':'S','B':'V','V':'B','N':'N','a':'t','t':'a','c':'g','g':'c','n':'n','r':'y','y':'r'}
# RevSeqList = list(reversed(seq))
# RevComSeqList = [ntComplement[k] for k in RevSeqList]
# print(RevComSeqList)
# RevComSeq = ''.join(RevComSeqList)
###################################
# a=open("007.txt","r")
# b=[]
# for i in a:
#     k=i.strip().split()
#     print(k)
# b=[i for i in range(len(k))]#构建连续自然数列表
# print(b)
# d1=dict(zip(b,k))
# print(d1)
#############################################
# d={}
# with open("011.txt","r") as fn2:
#     for i in fn2:
#         i=i.strip().split()
#         # print(i)
#         d[i[0]]=i[1:]
#     # print(d)
# with open("010.txt","r") as fn1:
#     for j in fn1:
#         j=j.strip().split()
#         if j[0] in d.keys():
#             print(j[1]+"\t"+"\t".join(d[j[0]]))
##########################################################
# a=open("021.txt","r")
# b=open("022.txt","w")
# c=[]
# d=[]
# for i in a:
#     i=i.strip()
#     # print(i)
#     # b.write(i+"\n")
#
#     i=i.split()
#     d=["-6"]*(10-len(i))
#     # print(10-len(i))
#     # d=["*"*j for j in range(10-len(i))]
#     # print(i[1:3])
#     c=i[0:1]+d[:]+i[int(1):len(i)]
#     print(c)
#     # print(" ".join(c))
#     # print(d)
#     # b.write(" ".join(c))
#     # d.write(" ".join(c)+"\n")
#######################################################
# d={}
# with open("011.txt","r") as fn2:
#     for i in fn2:
#         i=i.strip().split()
#         d[i[0]]=i[:]
#     print(d)
# with open("010.txt","r") as fn1:
#     for j in fn1:
#         j=j.strip().split()
#         if j[0] in d.keys():
#             print("\t".join(d[j[0]]+j[:]))
##################################################
# a=open("040.txt")
# for i in a:
#     i=i.strip().split()
#     i=i[0:1]+i[2:4]
#     print("\t".join(i))
######################################
# a=open("042.txt")
# for i in a:
#     i=i.strip().split()
#     m=[int(j) for j in i[1:]]
#     # print(sum(m))
#     print("".join(i[0:1])+":"+str(sum(m)/len(m)/6))
##########################################################
#用于计算多个同源序列的保守性
# import pandas as pd
#
# with open ("042.txt","r") as f1:
#     a=pd.read_table(f1,header=None,index_col=0)
#     # print(a)
#     a=a.dropna(axis=1)#按照列索引
#     a1=[]
#     list=[]
#     # print(a)
#     a_row_number=a.shape[0]#计算矩阵的行数
#     # print(a_row_number)#计算pandas的行数
#     # a.loc['Row_mean'] = a.apply(lambda x: x.sum())#计算列的和并把和作为新的一行
#     a.loc['Row_mean'] = a.apply(lambda x: x.mean())#计算列的平均值并把平均值作为新的一行
#     # print(a)
#     list=a.values.tolist()#把矩阵转换成列表
#     # print(list[16])
#     list1=list[a_row_number]#把列表中的最后一个元素，也就是平均值单独提取出来
#     list2=[str(i) for i in list1]
#     print("\t".join(list2))
# # def Get_Average(list):
# # 	sum=0
# # 	for i in list:
# # 		sum+=i
# # 	return sum/len(list)
# # ave=Get_Average(list1)
# # print (args.file1,ave)
####################################################
# d = {}
# chl_fasta = {}
# with open ("047.txt","r") as fn1:
#     for i in fn1:
#         i1=i.strip().split()
#         d[i1[0]]=1
# with open ("046.txt","r") as fn2:
#     for row in fn2:
#         if ">" in row:
#             fsy = row.split()
#             chl_gene = fsy[0].replace('>', '')
#             fsy_sequence = ''
#         else:
#             ro=row.strip()
#             # print(ro)
#             sequences = ro.split()
#             # print(row)
#             # print(sequences)
#             store = sequences[0]
#             # print(sequences[0])
#             fsy_sequence = fsy_sequence + store
#             chl_fasta[chl_gene] = fsy_sequence
#
# for i in d.keys():
#     if i in chl_fasta.keys():
#         # print(len(chl_fasta[i]))
#         print(">"+str(i)+"\n"+chl_fasta[i][len(chl_fasta[i])-3:len(chl_fasta[i])])
#     else:
#         continue
#######################################
# a=open("048.txt","r")
# sum=0
# n=0
# for i in a:
#     i=i.strip().split()
#     "".join(i)
#     print(i)

#     sum+=float(i[0])
#     n+=1
# print(sum/n)
#######################################
# d={}
# a=open("050.txt","r")
# b=open("051.txt","r")
# for i in a:
#     i=i.strip().split()
#     # print(i[0])
#     d[i[0]]=i[1]
# for j in b:
#     j=j.strip().split()
#     # print(j)
#     if j[0] in d.keys():
#         print(j[0]+"\t"+d[j[0]])
#     else:
#         print(j[0]+"\t"+"0")
#
# # print(d)
#############################
# a=open("meregetxt7-1.txt","r")
# b=open("meregetxt7-2.txt","w")
# for i in a:
#     i=i.strip().split()
#     a=int(i[0])
#     # print(i[1:a+1])
#     b.write("\t".join(i[1:a+1])+"\n")
########################################
# a=open("054.txt","r")
# for i in a:
#     i=i.strip().split()
#     # print(i)
#     i.reverse()
#     print("\t".join(i[len(i)-1:len(i)]+i[0:len(i)-1]))
#####################################
# a=open("055.txt","r")
# for i in a:
#     i=i.strip().split()
#     b=9-len(i)
#     # print(b)
#     c=["-6"]*b
#     # print(c)
#     print("\t".join(i[:]+c[:]))
###################################################
# a=open("054.txt","r")
# for i in a:
#     i=i.strip().split()
#     # print(i)
#     i.reverse()
#     print("\t".join(i))
###############################
# # d = {}
# chl_fasta = {}
#
# with open ("056.txt","r") as fn2:
#     for row in fn2:
#         if ">" in row:
#             fsy = row.split()
#             chl_gene = fsy[0].replace('>', '')
#             fsy_sequence = ''
#         else:
#             ro=row.strip()
#             # print(ro)
#             sequences = ro.split()
#             # print(row)
#             # print(sequences)
#             store = sequences[0]
#             # print(sequences[0])
#             fsy_sequence = fsy_sequence + store
#             chl_fasta[chl_gene] = fsy_sequence
# for i in chl_fasta.keys():
#     print(i,len(chl_fasta[i]))

# for i in d.keys():
#     if i in chl_fasta.keys():
#         # print(len(chl_fasta[i]))
#         print(">"+str(i)+"\n"+chl_fasta[i][len(chl_fasta[i])-3:len(chl_fasta[i])])
#     else:
#         continue
#######################################################################
#将列表强行拆解为两个列表
#方法1：

# letter_list = []
# num_list = []
# list1 = [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
# for i in list1:
#     letter_list.append(i[0])
#     num_list.append(i[1])
# print(letter_list)
# print(num_list)

#方法2：
# list1 = [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
#
# list_result = tuple(zip(*list1))
# letter_list = list(list_result[0])
# num_list = list(list_result[1])
# print(list_result)
# print(letter_list)
# print(num_list)
#或者
# list1 = [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
# letter_list, num_list = zip(*list1)
# print(letter_list)
# print(num_list)
#方法3：

# import pandas as pd
# list1 = [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
# df = pd.DataFrame(list1)
# # print(df)
# list = [df[x].values.tolist()  for x in df.columns]
# list2 = [df[x].values  for x in df.columns]
# print(list)
# print(list2)
# print(df[0].tolist())
# print(df[1].tolist())

#############################################
#计算数组中元素值为1的个数方法
# a = [1,0,2,0,1]
# b = list( filter(lambda x:x==1,a))
# print(b)
# print(f"1的个数：{len(b)}")

######################################################
#学习使用loc和iloc如何取行和列
#使用loc函数，索引的是字符串，前后都要取，是属于“前闭后闭”的情况
#:表示所有，[]里边为先行后列
#建议写df.loc[0, :]，这样可以清楚的看出为第0行的所有记录，同样如果取第’A’列的所有记录，可以写df.loc[:, ‘A’]
#iloc函数为Selection by Position，即按位置选择数据，即第n行，第n列数据，只接受整型参数
#注意iloc函数中df.iloc[:,1:3]=df.iloc[:,[1,2]]

#iloc函数,输出奇数行的方法：df.iloc[[0,2,4,6]]或者：df.iloc[0:8:2]
#iloc函数索引的是int型的数字，是属于前闭后开的。（注意~索引都是默认从0开始的~）
# import pandas as pd
#
# df=pd.read_table("045.txt",sep=" ",header=None)
# # print(df.iloc[0,:])#注意[]中是先行后列
# # df.loc[3,:]=range(4,8,1)#增加行,行名是3，内容是4，5，6，7
# df.loc[:,4]=range(5,8,1)#增加列，列名是4，增加的内容是5，6，7
# df1=pd.DataFrame(df)
# df1=pd.DataFrame(df,index=range(0,3,1),columns=list('ABCD'))
# print(df)
# a=[x for x in range(1,6)]
# df1=pd.DataFrame(a)
# print(df1)
###############################
# 索引练习
# import pandas as pd
# print(pd.Index([1,2,3]))
# print(pd.Index(list('abc')))
# print(pd.Index(list('abc'),name="something"))
# print(pd.interval_range(start=0,end=5))#间隔索引
#多层索引：多个层次，且有归属关系的索引
# arrays=[[1,1,2,2],['red','blue','red','blue']]
# print(pd.MultiIndex.from_arrays(arrays,names=('number','color')))
#数字索引
# print(pd.RangeIndex(1,100,2))
###############################################
# import pandas as pd
# df=pd.read_table("044.txt",sep=" ")
# print(len(df))
#
# s1=pd.Series(["a","b"])
# s2=pd.Series(["c","d"])
# # print(pd.concat([s1,s2]))
# print(pd.concat([s1,s2],keys=['s1','s2'],names=['Series name','Row ID']))

###
# df1=pd.DataFrame([[1,2],[3,4]],columns=list('AB'))
# df2=pd.DataFrame([[5,6],[7,8]],columns=list('AB'))
# print(pd.concat([df1,df2],axis=1))
#################################################
# import pandas as pd
# import numpy as np
# df=pd.read_table("044.txt",sep=" ")
# print(df)
#df.itertuples()产生tuples
# for row in df.itertuples(index=False,name="liji"):
#     print(row)

# for label,ser in df.items():
#     print(label)
#     print(ser[:3],end='\n\n')

# print(df)
#map()函数用法：
# print(df.team.map({'A':'一班','B':'二班','C':'三班','D':'四班'}))
#map应用函数
# def f(x):
#     return len(str(x))
# print(df['name'].map(f))
####分组
# print(df.groupby('team').agg({'math':[sum,'std',max],'Chinese':'count','English':'mean'}))
#
# print(df.math.groupby(df.team).sum())
# a=df.groupby('team')
# print(a)
#查询pd.DataFrame.groupby的使用方法
# print(help(pd.DataFrame.groupby))
#使用分组器groupby学习
# print(df.groupby(pd.Grouper('name')).sum())
#groupby操作后分组字段会成为索引，使用as_index=False,可以拒绝此情况
# print(df.groupby('team',as_index=False).sum())
# print(df.drop('name',axis=1).groupby('team').sum())
#返回每组中数学成绩最高的前两名
# def first_2(df_,c):
#     return df_[c].sort_values(ascending=False).head(2)
# a=df.set_index('name').groupby('team').apply(first_2,'math')
# print(a)
#####
# def f_mi(x):
#     d=[]
#     d.append(x['math'].sum())
#     d.append(x['Chinese'].max())
#     d.append(x['English'].mean())
#
#     return pd.Series(d,index=[['math','Chinese','English'],['sum','max','mean']])
# print(df.groupby('team').apply(f_mi))
######
# idx=pd.date_range('1/1/2020',periods=100,freq='T')
# df2=pd.DataFrame(data={'a':[0,1]*50,'b':1},index=idx)
# print(df2.groupby('a').resample('20T').sum())
#######
# a=open("01.txt","r")
# for i in a:
#     i=i.strip().split()
#     print(i[0])
#     # a=int(i[0])
#     # print(i[1,1+a])

# a=open("02.txt","r")
# for i in a:
#     i=i.strip().split()
#     j=list(i[0])
#     b=len(j)
#     # j=[str(x) for x in i]
#     # k=list(j)
#     print("".join(j[b-2:b]))
#     print(b)
#     # print(i[0])

##########################################
# a=open('rice_arabidopsis-1.txt','r')
# b=open('rice_arabidopsis-2.txt','w')
# # a=open('100.txt','r')
# # b=open('101.txt','w')
# for i in a:
#     i=i.strip().split()
#     print(b.write(" ".join(i)+"\n"))


#############################################
# import re
# a=open("103.txt","r")
# b=open("105.txt","r")
# c={}
# # n=4
# for i in a:
#     i=i.strip().split()
#     # print(i)
#     for j in range(4):
#         c[i[j]]=i[:]
#
# # print(c)
#
# for j in b:
#     j=j.strip().split()
#     # k=re.search('.*4',c[j[0]])
#     if j[0] in c.keys():
#         print(" ".join(c[j[0]]))
#     else:
#         continue
#     # if j[0] in c.keys():
#     #     print(j[0],c[j[0]])
#     # else:
#     #     continue

# n = 7
# while n >= 0:
#     print (' ' * (7-n) + '* ' * n)
#     n -= 2

# a=[]
# for i in range(2,10):
#     count=0
#     for x in range(2,i-1):
#         if i % x ==0:
#             count+=1
#     if count ==0:
#         a.append(i)
# print(a)
# print(66!=66)
# a=3
# b=4
# a=a*b
# print(a)

# x=371
# print(x%100//10)
# a,b=1,2
# print(a)

#############################
# from atexit import register
# from re import compile
# from threading import Thread
# from time import ctime
# from urllib.request import urlopen as uopen
# REGEX=compile('#([\d,]+)in Books')
# AMZN='https://amazon.com/dp/'
# ISBNs={
#     '0132269937':'Core Python Programming',
#     '0132356139':'Python Web Development with Django'
# }
# def getRanking(isbn):
#     page=uopen('%s%s'%(AMZN,isbn))#or str.format()
#     data=page.read()
#     page.close()
#     return REGEX.findall(data)[0]
# def _showRanking(isbn):
#     print('_%r ranked %s'%(ISBNs[isbn],getRanking(isbn)))
#
# def main():
#     print ('At',ctime(), 'on Amazon...')
#     for isbn in ISBNs:
#         _showRanking(isbn)
# @register
# def _atexit():
#     print('all done at: ',ctime())
# if __name__ =='__main__':
#     main()

# from atexit import register
# from re import compile
# from threading import Thread
# from time import ctime
# from urllib.request import urlopen as uopen
# REGEX=compile('#([\d,]+)in Books')
# AMZN='http://amazon.com/dp/'
# ISBNs={
#     '0132269937':'Core Python Programming',
#     '0132356139':'Python Web Development with Django',
# }
# def getRanking(isbn):
#     page=uopen('%s%s'%(AMZN,isbn))#or str.format()
#     data=page.read()
#     page.close()
#     return REGEX.findall(data)[0]
# def _showRanking(isbn):
#     print('_%r ranked %s'%(ISBNs[isbn],getRanking(isbn)))
#
# def main():
#     print ('At',ctime(), 'on Amazon...')
#     for isbn in ISBNs:
#         _showRanking(isbn)
# @register
# def _atexit():
#     print('all done at: ',ctime())
# if __name__ =='__main__':
#     main()
################################
# import pandas as pd
# import numpy as np
# df=pd.read_table("fuz2-1.txt")
# # print(df)
# pd.set_option('display.width',None)
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_colwidth',None)
# # df1=df.set_index("ID")
# # a=open("110.txt","r")
# # b=open("111.txt","r")
# # print(df)
# df['Class']=df['Class'].astype(str)
# df1=df.groupby(["ID"]).apply(lambda x:['::'.join(x['Class'])])
# # print(df1)
# # df1.to_csv('lijifirstcolumn-1.txt',sep=' ',index=0,header=0)
# df1.to_csv('fuz2-1.csv')



###############################################
#! /usr/bin/env python
#usage: python hash-always.py -f1 1.txt -f2 2.txt > out.txt
# import argparse
# parser = argparse.ArgumentParser(description="Advanced screening always by hash")
# parser.add_argument("-f1","--file1",help="可以理解为key")
# parser.add_argument("-f2","--file2",help="可以理解为字典")
# args = parser.parse_args()
#
# d = {}
# chl_fasta = {}
# with open (args.file1,"r") as fn1:
#     for i in fn1:
#         i1=i.strip().split()
#         d[i1[0]]=1
# with open (args.file2,"r") as fn2:
#     for row in fn2:
#         if ">" in row:
#             fsy = row.split()
#             chl_gene = fsy[0].replace('>', '')
#             fsy_sequence = ''
#         else:
#             ro=row.strip()
#             # print(ro)
#             sequences = ro.split()
#             # print(row)
#             # print(sequences)
#             store = sequences[0]
#             # print(sequences[0])
#             fsy_sequence = fsy_sequence + store
#             chl_fasta[chl_gene] = fsy_sequence
#
# for i in d.keys():
#     if i in chl_fasta.keys():
#         print(">"+str(i)+"\n"+chl_fasta[i])
#     else:
#         continue


#####################
# a=open("50.txt","r")
# for row in a:
#     # i=list(i)
#     if ">" in row:
#         fsy= row.split()
#         chl_gene = fsy[0].replace('>', '')
#         fsy_sequence = ''
#     else:
#         ro=list(row)
#         roa=ro[0:3]
#
#         roa.reverse()
#         print("".join(roa))

#####################################
#逆向输出，倒叙输出
# a=open("53.txt","r")
# a1=open("5UTR+200bp+LOC_Os03g21120.1.fasta123","r")
# b1=open("5UTR+200bp+LOC_Os03g21120.1.fasta123reserve","w")
# for i in a1:
#     i=i.strip().split()
#     b=len(i)
#     b1.write(i[0]+"\t"+"\t".join(i[b:0:-1])+"\n")

###################################################
# import pandas as pd
# df=pd.read_csv("At5utr200bp6bra16844merge1sortedreplacefillupreverse.csv")
# df1=df.T
# # print(df.T)
# df1.to_csv("At5utr200bp6bra16844merge1sortedreplacefillupreversezhuanzhi.csv",header=None)

# df2=pd.read_csv("At5utr200bpmerge1sortedreplacefillupreversezhuanzhi.csv")
# print(df2.head())





######################################################################
# a=open("060.txt","r")
# b=0
# n=0
# for i in a:
#     i=i.strip()
#     # print(len(i))
#     while b<(len(i)-1):
#         # if i[b]==".":
#         if (i[b]=="." and i[b+1]=="(" ) or (i[b]==")" and i[b+1]=="("):
#             n=n+1
#         if (i[b] == "." and i[b + 1] == ")") or (i[b] == ")" and i[b + 1] == ")"):
#         b=b+1
#     print(n)


####################
# a=open('5.txt','r')
# n=0
# for i in a:
#     if i.endswith("\n"):
#         n+=1
#     else:
#         continue
# print(n)


##########################
# import pandas as pd
# df=pd.read_table("6.txt",header=None)
#
# for i in range(1,len(df)):
#     print(df.iloc[i,0]/df.iloc[0,0])

################################################
# a=open('7.txt','r')
# n=0
#
# for i in a:
#     i=i.strip()
#     if i.startswith("_") and i.endswith("_"):
#         print("Os")

################################################
# #把字符串变成列表，并逆向输出
# a=open("8.txt","r")
# b=open("9.txt","w")
# for i in a:
#     i=i.strip()
#     j=list(i)
#     j.reverse()
#     # i=i.split()
#     # b=len(i)
#     # j=i[b::-1]
#     b.write("".join(j)+"\n")
#     # print("".join(j)+"\n")

##############################################
# #计算重复的反向stem sequence
# a=open("4352.txt","r")
# c=open("4352-1.txt","w")
# b=[]
#
# for i in a:
#     i=i.strip().split()
#     # print(len(i))
#     for m in range(len(i)):
#
#         a1=list(i[m])
#         a2="".join(a1[::-1])
#         if a2 in i[m+1:]:
#             b.append(i[m])
#     c.write(";".join(b))
################################################
#重点，按行输出的python脚本，从网上摘抄的，需要认真剖析
# def print_lines(file_name, lines_num):
#     f = open(file_name, "r")
#     ###确定开始行和结尾行
#     lines_list = lines_num.split(sep=":")
#     start_line = lines_list[0]
#     end_line = lines_list[1]
#     ###将文件按行排列在列表中方便打印
#     f_list = []
#     for eachline in f:
#         f_list.append(eachline)
#
#     if start_line == "" and end_line == "":
#         print(f"文件{file_name}的全文内容如下：")
#         start_index = 0
#         end_index = len(f_list)
#     elif start_line == "":
#         print(f"文件{file_name}从开始到第{int(end_line)}行的内容如下：")
#         start_index = 0
#         end_index = int(end_line)
#     elif end_line == "":
#         print(f"文件{file_name}从第{int(start_line)}行到末尾的内容如下：")
#         end_index = len(f_list)
#         start_index = int(start_line) - 1
#     else:
#         print(f"文件{file_name}从第{int(start_line)}行到{int(end_line)}的内容如下：")
#         start_index = int(start_line) - 1
#         end_index = int(end_line)
#     ####按要求打印文件内容
#     for i in range(start_index, end_index):
#         print(f_list[i])
#
#     f.close()
#
#
# file_name = input(" 请输入")
# lines_num = input("请输入需要显示文件的行数[格式如13:21或：21或21:]：")
# print_lines(file_name, lines_num)

########################################################################
#统计RNA二级结构的类型
# a=open("AT1G01060.4.st.8linetoendline","r")
# B=0
# E=0
# H=0
# I=0
# M=0
# P=0
# S=0
# s=0
# for i in a:
#     i=i.strip()
#     if i.startswith("B"):
#         B+=1
#     elif i.startswith("E"):
#         E+=0
#     elif i.startswith("H"):
#         H+=0
#     elif i.startswith("I"):
#         I+=0
#     elif i.startswith("M"):
#         M+=0
#     elif i.startswith("P"):
#         P+=0
#     elif i.startswith("S"):
#         S+=0
#     elif i.startswith("s"):
#         s+=0
# print("B："+str(B))

###################################################
# #MSUx.txt
# c={}
# with open("12.txt","r") as f1:
#
#     for i in f1:
#         i = i.strip().split()
#         # print(i)
#         for j in range(4):
#             c[i[j]] = i[:]
#
# with open("13.txt", "r") as f2:
#     for j in f2:
#         j = j.strip().split()
#         if j[0] in c.keys() and j[1] in c[j[0]]:
#             print(" ".join(c[j[0]]))
#         else:
#             continue

########################################################
# a=open("14.txt","r")
# a1=[]
# b1=[]
# b=open("15.txt","r")
# for i in a:
#     i=i.strip().split()
#     a1.append(i)
# for j in b:
#     j = j.strip().split()
#     b1.append(j)
#
#     # print("".join(i)+"\n"+"".join(j))
# for i,j in zip(a1,b1):
#     print("".join(i)+"\n"+"".join(j))

#######################################################
#批量把两个文件合并到一起
# def merge(m,n):
#     m2=[]
#     n2=[]
#     with open(m,"r") as m1:
#         for i in m1:
#             i=i.strip().split()
#             m2.append(i)
#     with open(n,"r") as n1:
#         for j in n1:
#             j=j.strip().split()
#             n2.append(j)
#             # print("".join(i)+"".join(j)+"\n")
#     for i,j in zip(m2,n2):
#         print(str(m),"".join(i),"".join(j))
#
# a=open("17.txt","r")
# for i in a:
#     i=i.strip().split()
#     m=i[0]
#     n=i[1]
#     # print(m)
#     merge(m,n)
###########################################################
# a=open("18.txt","r")
# b=open("19.txt","r")
# d1={}
# d2={}
# for i in a:
#     i=i.strip().split()
#     d1[i[0]]=i[1:3]
# # print(dict)
# for j in b:
#     j=j.strip().split()
#     d2[j[0]]=1
# for m in d2.keys():
#     if m in d1.keys():
#         print(";".join(d1[m]))
############################################################
# a=open("20.txt","r")
# for i in a:
#     i=i.strip()
#     # b=int(len(i)/2)
#     c=int(len(i))
#     # i=i.split()
#     # print(b)
#     # for j in i:
#     # #     print(j[1])
#     # for m in range(b):
#     #     print(i[m]+":"+i[b-m])
#     print(i[0]+":"+i[c-1])
#     # print(i)
############################################################
# a=open("21.txt","r")
# c=open("22.txt","w")
# b=1
# c=[]
# m=0
# for i in a:
#     i=i.strip().split()
#     c.append(i)
#     d=c[0]
#
# while m <=len(d)-1:
#     print(d[m]+":"+d[m+1])
#     m+=2

#############################################################
# a=open("22.txt","r")
# m=0
# n=0
# for i in a:
#     i=i.strip().split()
#     m=int(len(i)/2)
#     j=list(i[len(i)-1])
#     if i[0]=="".join(j[::-1]):
#         n=m
#     else:
#         n=m+1
#     print(m,n)
    # j="".join(j[::-1])
    # print(j)

###################################################

# def convert01(file1):
#     newlist=[]
#     n=0
#     for i in file1:
#         eachline = i.strip()
#         n = n + 1
#         if eachline.startswith(">"):#把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
#             print(eachline)
#             # b.write(eachline+"\n")
#         else:
#             if n ==2:
#                 # print(eachline)
#                 for i in eachline:
#                     i = i.strip("\n").split()
#                     i = "".join(i)
#                     if i == "A":
#                         newlist.append("1")
#                     elif i == "T":
#                         newlist.append("1")
#                     elif i == "C":
#                         newlist.append("1")
#                     elif i == "G":
#                         newlist.append("1")
#                     elif i == "X":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#                     # print("".join(newlist))
#                     # newlist = ["1" for i in eachline]
#                 print("\t".join(newlist))
#                 # b.write("".join(newlist)+"\n")
#                 dz = eachline
#             else:
#                 newlist = []
#                 for i,j in zip(eachline,dz):
#                     if i==j and i!="-":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#                 print("\t".join(newlist))
# from multiprocessing import Pool
#
# import argparse
# parser = argparse.ArgumentParser(description="Advanced screening always by hash")
# parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
# args = parser.parse_args()
# with open(args.file1,"r") as f1:
#     pool=Pool(2)
#     convert01(f1)
###############################################################################
# 计算ATG的位置
# def filter_length01(base):
#     list01=[]
#     for j in range(len(base)):
#         if base[j] !="-":
#             list01.append(base[j])
#         else:
#             continue
#     return (int(len(list01)))
# def filter_length02(base):
#     list01=[]
#     for j in range(len(base)):
#         list01.append(base[j])
#     return (int(len(list01)))
# a=open("29.txt","r")
# a1=0
# b=0
# n=0
# m=0
# for i in a:
#     i=i.strip()
#     n+=1
#     if i.startswith(">"):
#         # print(i)
#         continue
#     else:
#
#         if n==2:
#             b=str(i)
#     # print(filter_length(b))
#         # length=len(i)
#             for j in range(len(b)):
#                 if "".join(i[j:j+3])=="ATG":
#                     c=str(i[0:j+3])
#                     # a1=filter_length02(c)
#
#                     # print(c)
#                     if filter_length01(c)==10:
#                         m+=1
#                         a1=filter_length02(c)
#                         # print(a1)
#         else:
#             for k in range(len(b)):
#                 if "".join(i[k:k+3])=="ATG":
#                     c=str(i[0:k+3])
#                     a2=filter_length02(c)
#                     # print(a2)
#                     if filter_length01(c)==10 and a2==a1:
#                         m+=1
#                     else:
#                         continue
#                         # print("yes1")
# print(m)

######################################################
#去除fasta的title
# a=open("30.txt","r")
# for i in a:
#     i=i.strip()
#     if i.startswith(">"):
#         continue
#     else:
#         print(i)
################################
# 序列比对之后，截取UTR
# def filter_length01(base):
#     list01=[]
#     for j in range(len(base)):
#         if base[j] !="-":
#             list01.append(base[j])
#         else:
#             continue
#     return (int(len(list01)))
# # def filter_length02(base):
# #     list01=[]
# #     for j in range(len(base)):
# #         list01.append(base[j])
# #     return (int(len(list01)))
# a=open("29.txt","r")
#
# n=0
# for i in a:
#     i=i.strip()
#     n+=1
#     if i.startswith(">"):
#         print(i)
#         # continue
#     else:
#
#         if n==2:
#             b=str(i)
#     # print(filter_length(b))
#         # length=len(i)
#             for j in range(len(b)):
#                 if "".join(i[j:j+3])=="ATG" or "ATC":
#                     c=str(i[0:j+3])
#                     # a1=filter_length02(c)
#
#                     # print(c)
#                     if filter_length01(c)==10:
#                         print("".join(i[j+3:]))
#                         # a1=filter_length02(c)
#                         a1=len(c)
#                         # print(a1)
#         else:
#             for k in range(len(b)):
#                 if "".join(i[k:k+3])=="ATG" or "ATC":
#                     c=str(i[0:k+3])
#                     # a2=filter_length02(c)
#                     a2=len(c)
#                     # print(a2)
#                     if filter_length01(c)==10 and a2==a1:
#                         print("".join(i[k+3:]))
#                     else:
#                         continue
#                         # print("yes1")
# # print(m)
###############################################################
#fasta格式转aln格式  01版
# a=open("30.txt","r")
# seq={}
# print("ClUSTAL"+"\n")
# for i in a:
#     # i=i.strip()
#     # print(i)
#     if i.startswith(">"):
#         name=i.strip().split('>')[1]
#         # i=i.replace(">","")
#         # print(i)
#         seq[name]=""
#     else:
#         seq[name]+=i.replace("\n","")
# for i in seq.keys():
#     print(i+" "+seq[i])
##########################################################
#fasta格式转aln格式02版非fasta格式转为aln  02版
# a=open("32.txt","r")
# print("ClUSTAL"+"\n")
# for i in a:
#     i=i.strip().split()
#     # i="".join(i)
#     # print(i[0])
#     print(str(i[0])+" "*10+"".join(i[1:]))
####################################################################
# a=open("31.txt","r")
# def function01(a):
#     n = 0
#     newlist = []  # 创建一个列表
#     for i in a:
#         eachline = i.strip()
#         n = n + 1
#         if eachline.startswith(">"):#把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
#             # eachline = eachline.strip().split('>')[1]
#             #
#             # newlist.append("\n"+eachline)
#             # newlist.append(eachline)
#             continue
#         else:
#             if n ==2:
#                 # print(eachline)
#                 for i in eachline:
#                     i = i.strip("\n").split()
#                     i = "".join(i)
#                     if i == "A":
#                         newlist.append("1")
#                     elif i == "T":
#                         newlist.append("1")
#                     elif i == "C":
#                         newlist.append("1")
#                     elif i == "G":
#                         newlist.append("1")
#                     elif i == "X":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#                     # print("".join(newlist))
#                     # newlist = ["1" for i in eachline]
#                 # b.write("".join(newlist)+"\n")
#                 dz = eachline
#             else:
#                 for i,j in zip(eachline,dz):
#                     if i==j and i!="-":
#                         newlist.append("1")
#                     else:
#                         newlist.append("0")
#     return (" ".join(newlist))
#
# def sum_of_dataframe(a):
#     list01 = []
#     n = 0
#     for i in a:
#         if i != "0" and i != "1":
#             continue
#             # list01.append(i)
#         else:
#             # continue
#             list01.append(i)
#     # print(list01)
#     for i in list01:
#         n += int(i)
#     print(n)
#
#
#
# a3=open("31.txt","r")
# a4=function01(a3)
# sum_of_dataframe(a4)

############################################################
#去除拟南芥gap以及gap下面对应的其他物种的所有的序列
# newlist = []#创建一个列表
# # b=open("out1.sequence.txt","w")
# a=open("34.txt","r")
# n=0
# for i in a:
#     eachline = i.strip()
#     n = n + 1
#     if eachline.startswith(">"):  # 把以">"开头的，打印出来，意思是把fasta序列的表头打印出来
#         print(eachline)
#         # b.write(eachline+"\n")
#     else:
#         if n == 2:
#             # print(eachline)
#             for i in eachline:
#                 i = i.strip("\n").split()
#                 i = "".join(i)
#                 if i in "ATGC":
#                     newlist.append(i)
#             print("".join(newlist))
#             # b.write("".join(newlist)+"\n")
#             dz = eachline
#         else:
#             newlist1 = []
#             for i,j in zip(eachline,dz):
#                 if j != "-":
#                     newlist1.append(i)
#             print("".join(newlist1))
#################################################################
# newlist=[]
# a=open("35.txt","r")
# for i in a:
#     i=i.strip("\n").split(" ")
#     # print(i)
#     # i=" ".join(i)
#     if len(i)==1:
#         continue
#     else:
#         print("\t".join(i))

################################################################

# a=open("35.txt","r")
# seq={}
# for i in a:
#     if i.startswith(">"):
#         name = i.strip().split('>')[1]
#         seq[name]=""
#     else:
#         seq[name]+=i.replace("\n", "")
# for i in seq.keys():
#     if seq[i] !="":
#         print(i + " " * 10 + seq[i])
#     # print(i)
###########################################
# import pandas as pd
# df=pd.read_table("36.txt",header=None)
# def remove_the_blank(a):
#     newlist = []
#     for i in a:
#         i = i.strip("\n").split()
#         i = " ".join(i)
#         if len(i) == 1:
#             continue
#         else:
#             newlist.append(i+"\n")
#     return ("".join(newlist))
#
#
# a=open("36.txt","r")
# n=0
# b=remove_the_blank(a)
# # df=pd.read_table(b,header=None)
# # print(df)
# for i in b:
#     if i.endswith("\n"):
#         n+=1
# print(n)
###########################################
# a=open("35.txt","r")
# seq={}
# for i in a:
#     if i.startswith(">"):
#         name = i.strip().split('>')[1]
#         seq[name]=""
#     else:
#         seq[name]+=i.replace("\n", "")
# n=0
# for i in seq.keys():
#     if seq[i] !="":
#         # print(">"+i + " " * 10 + seq[i])
#         n+=1
# print(n)
############################################
# 序列比对之后，截取UTR
# def filter_length01(base):
#     list01=[]
#     for j in range(len(base)):
#         if base[j] !="-":
#             list01.append(base[j])
#         else:
#             continue
#     return (int(len(list01)))
# # def filter_length02(base):
# #     list01=[]
# #     for j in range(len(base)):
# #         list01.append(base[j])
# #     return (int(len(list01)))
# a=open("38.txt","r")
#
# n=0
# for i in a:
#     i=i.strip()
#     # print(i)
#     n+=1
#     if n==1:
#         b=str(i)
#         # print(b)
# # print(filter_length(b))
#     # length=len(i)
#         for j in range(len(b)):
#             b1="".join(i[j:j+3])
#             # print(str(b1))
#             if (str(b1)=="788") or (str(b1)=="789"):
#                 # print(str(b1))
#                 c=str(i[0:j+3])
#                 # a1=filter_length02(c)
#
#                 # print(c)
#                 if filter_length01(c)==9:
#                     print("".join(i[j+3:]))
#                     a1=len(c)
#                     # print(a1)
#     else:
#         for k in range(len(b)):
#             if ("".join(i[k:k+3])=="788") or ("".join(i[k:k+3])=="789"):
#                 c2=str(i[0:k+3])
#                 a2=len(c2)
#                 # print(a2)
#                 if (filter_length01(c2)==9) and (a2==a1):
#                     print("".join(i[k+3:]))
#                 else:
#                     continue
#                     # print("yes1")
# # print(m)

# a=open("38.txt","r")
# n=0
# for i in a:
#     i=i.strip()
#     # print(i)
#     n+=1
#     if n==1:
#         b=str(i)
#         for j in range(len(b)):
#             c="".join(i[j:j+3])
#             d=len("".join(i[0:j+3]))
#             if (str(c)=="789") and (d==15):
#                 print(c,d)
#     else:
#         for k in range(len(b)):
#             if "".join(i[k:k+3])==""

########################################################


