# import numpy as np
# a=open("sequence_covariation01.txt","r")
# b=[]

# A = np.zeros((4,6), dtype=str)  # 先创建一个全零方阵A，并且数据的类型设置为float浮点型
#
# lines = a.readlines()  # 把全部数据文件读到一个列表lines中
# print(lines)
# A_row = 0  # 表示矩阵的行，从0行开始
# for line in lines:  # 把lines中的数据逐行读取出来
#     list = line.strip('\n')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
#     print(list[0:3])
#     A = list[0:3]  # 把处理后的数据放到方阵A中。list[0:4]表示列表的0,1,2,3列数据放到矩阵A中的A_row行
#     print(type(A))
    # A_row += 1  # 然后方阵A的下一行接着读
# for i in A:
#     print(i)
# print(A[0,0])
# points=np.array(i)
# print(points)
# print(type(points))
# b={}
# filelist = a.readlines()            #将txt文件转换为所有的行组成的列表
# numberoflines =len(filelist) #得到行数
# print(filelist)

# print ("行数: %s" % (numberoflines))
# returnMat = np.zeros((numberoflines,3)) #生成一个numberoflines行，3列的矩阵
# print(returnMat)
# for i in a:
#     a=a.strip('\n').split('')
#     print(i)

# from numpy import *
#
# A = zeros((4, 4), dtype=float)  # 先创建一个全零方阵A，并且数据的类型设置为float浮点型
#
# f = open('d:\\b.txt')  # 打开数据文件文件
# lines = f.readlines()  # 把全部数据文件读到一个列表lines中
# A_row = 0  # 表示矩阵的行，从0行开始
# for line in lines:  # 把lines中的数据逐行读取出来
#     list = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
#     A[A_row:] = list[0:4]  # 把处理后的数据放到方阵A中。list[0:4]表示列表的0,1,2,3列数据放到矩阵A中的A_row行
#     A_row += 1  # 然后方阵A的下一行接着读
# print(A)


import numpy as np

a=open("sequence_covariation01.txt","r")
# data_lists = a.readlines()	#读出的是str类型
b=open("sequence_covariation02.txt","w")
dataset= []
# 对每一行作循环
for data in a:
    data1 = data.strip('\n')	# 去掉开头和结尾的换行符
    data2=list(data1)
    # data2 = data1.split(' ')	# 把tab作为间隔符
    # data3=str(data1)
    # print(data3)
    dataset.append(data2)	# 把这一行的结果作为元素加入列表dataset
    # print(dataset)

dataset = np.array(dataset)
# print(dataset[3,3])
c=[]
j=0
while j <= 5:
    for i in range(4):
        if dataset[i,j]==dataset[0,j]:
            c.append(1)
        else:
            c.append(0)
        i=i+1
        # c.append("\n")
        # print(c)
    j=j+1
    c.append("\n")
print(c)
b.write(str(c))