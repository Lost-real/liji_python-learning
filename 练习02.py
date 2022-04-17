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
'''
下面是生成乘法口诀的代码：如下所示
1*1=1
1*2=2 2*2=4
'''
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
a=["A","B","C","D"]
b=["a","b","c","d"]
dic={}
for i in a:
    for j in b:
        dic{i}=j
