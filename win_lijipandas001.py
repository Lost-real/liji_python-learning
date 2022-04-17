import pandas as pd
with open ("ztotgen31spAT1G01120.1-5.txt","r") as f1:
    a=pd.read_table(f1,header=None,index_col=0)
    a=a.dropna(axis=1)#axis=1的含义是按照列索引，axis=0的含义是按照行索引
    a1=[]
    list=[]
    # print(a)
    a_row_number=a.shape[0]#计算矩阵的行数
    # print(a_row_number)#计算pandas的行数
    # a.loc['Row_mean'] = a.apply(lambda x: x.sum())#计算列的和并把和作为新的一行
    a.loc['Row_mean'] = a.apply(lambda x: x.mean())#计算列的平均值并把平均值作为新的一行
    # print(a)
    list=a.values.tolist()#把矩阵转换成列表
    # print(list[16])
    list1=list[a_row_number]#把列表中的最后一个元素，也就是平均值单独提取出来
    # print(list1)
    a1=[i for i in range(len(list1))]
    # print(a1)
    a2=[i for i in list1]
    a3=dict(zip(a1,a2))#使用zip构建字典
    # print(a3)
    b=[]
    #下面是使用滑动的方法
    n=80
    while n <= 100:
        for i in range(len(a1)):
            c = a1[i:i+n]
            # print(c)
            d = 0
            if len(c) == n:

                for j in c:
                    d+=a3.get(j, 100)
                d=d/n
                b.append(d)
            else:
                pass
        n += 1
# print(b)

m = 0
for i in b:
    if i >= 0.8:
        m += 1
        # print(a1[b_pos:b_pos+5])
        # print(a2[b_pos:b_pos+5])
    else:
        continue
print(m)

    # for i in range(len(list1)):
    #     c=list1[i:i+100]
    #     # print(c)
    #     d=0
    #     if len(c)==100:
    #         for j in c:
    #             d+=int(a3.get(j,100))
    #         b.append(d)
    #     else:
    #         pass
    #     # print(b)
    # max_value=max(b)
    # max_pos=b.index(max_value)
    # print(a1[max_pos:max_pos+100])
    # print(a2[max_pos:max_pos+100])