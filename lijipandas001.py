import pandas as pd
with open ("ztotgen31spAT1G01120.1-5.txt","r") as f1:
    a=pd.read_table(f1,header=None,index_col=0)
    a=a.dropna(axis=1)#按照列索引
    a1=[]
    list=[]
    # print(a)
    a_row_number=a.shape[0]
    # print(a_row_number)#计算pandas的行数
    # a.loc['Row_mean'] = a.apply(lambda x: x.sum()/a_row_number)#计算列的平均值并把和作为新的一列
    a.loc['Row_mean'] = a.apply(lambda x: x.mean())#计算列的平均值并把和作为新的一列
    # print(a)
    list=a.values.tolist()
    # print(list[16])

    list1=list[a_row_number]
    # print(list1)
    a1=[i for i in range(len(list1))]
    # print(a1)
    a2=[i for i in list1]
    a3=dict(zip(a1,a2))
    # print(a3)
    b=[]
    for i in range(len(list1)):
        c=list1[i:i+100]
        # print(c)
        d=0
        if len(c)==100:
            for j in c:
                d+=int(a3.get(j,100))
            b.append(d)
        else:
            pass
        # print(b)
    max_value=max(b)
    max_pos=b.index(max_value)
    print(a1[max_pos:max_pos+100])
    print(a2[max_pos:max_pos+100])