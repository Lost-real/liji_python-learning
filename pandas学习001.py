#计算矩阵中最大值的位置
# import pandas as pd
#
# df=pd.read_csv("55.txt",header=None,sep=" ",index_col=0)
# print(df[df==df.max().max()].dropna(how="all").dropna(how="all",axis=1))

#计算相关性最强的两个变量
# import pandas as pd
#
# df=pd.read_csv("56.txt",sep=" ")
# #ascending=Fasle的意思是降序排列
# print(df.corr().stack().sort_values(ascending=False).loc[lambda x:x<1].idxmax())

#同组数据转为同一行
# import pandas as pd
#
# df=pd.read_csv("57.txt",sep=" ")
# # print(df.pivot(index=['A','B','C'],columns='D',values='D'))
#
# print(df.groupby(['A','B','C']).apply(lambda x: ",".join(x.D.astype(str))).str.split(',',expand=True))

#
# import pandas as pd
# df=pd.read_csv("team.csv")
# print(df)


#pandas链式方法初体验
# import pandas as pd
# df=pd.read_csv("team.csv")
# print(df.groupby('team').first().assign(avg=lambda x: x.mean(1)).reset_index().set_index('name').query('avg>60').loc[:,['team','avg']])

#
# import pandas as pd
# df=pd.read_table('58.txt',sep=" ")
# # print(df.astype({'date': 'datetime64[ns]'}))
# # print(df.info)
# df01=df.astype({'date': 'datetime64[ns]'}).set_index('date').groupby([lambda x:x.month,lambda x:x.day]).apply(lambda x:x.gmv)
# # print(df.shape)
# print(df01)





#############################
# import pandas as pd
# df=pd.read_csv("pandas之行列转换04.csv",encoding='gbk')
# # df1 = df["info"].str.split(',').apply(pd.Series)
# df1 = df["info"].str.split(',').apply(pd.Series)
# # df1 = df["info"].apply(pd.Series)
# print(df1)

##############################
# import pandas as pd
# df=pd.read_csv("team.csv")
# # print(df)
# # df.groupby(lambda x: 'Q' in x,axis=1).sum()
#
# # print(df.groupby(lambda x: x%2==0).sum())
# # print(df.groupby(lambda x: 'Q' in x,axis=1).sum())
# df01=df.groupby(['team',df.name.str[0]])
# print(df01.get_group(('B','A')))
# print(df)

#######################################
# import pandas as pd
# df=pd.read_csv("Gradifferentstructuretypes.csv")
# print(df.drop('id',axis=1).groupby("type").sum())

######################################

# import pandas as pd
# df=pd.read_csv("禾本科 multiloop branch 长度和closing pair分布.csv")
# df01=pd.pivot(df,index="x",columns="y",values="number")
# df01.to_csv("禾本科 multiloop branch 长度和closing pair分布1.csv")

##########################################################
# import pandas as pd
# df=pd.read_csv("十字花科5UTR_bulge中3'closing pair频数统计1.csv")
# df01=pd.pivot(df,index="length",columns="type",values="number")
# df01.to_csv("十字花科5UTR_bulge中3'closing pair频数统计2.csv")
##################################################################
# import pandas as pd
# df=pd.read_csv("十字花科5UTR_internal loops3'closing pair频数统计.csv")
# df01=df.groupby("type").count()
# df01.to_csv("十字花科5UTR_internal loops3'closing pair频数统计1.csv")
#########################################################################
# import pandas as pd
# df=pd.read_table("23.txt",header=None)
# # print(df.shape[0])
# for i in range(0,df.shape[0]):
#     print(df.shape[0],df.iloc[i,0])

#####################################################################
#这个代码牛逼，实现了长数据变宽数据！！！
#这个代码牛逼，实现了长数据变宽数据！！！
#这个代码牛逼，实现了长数据变宽数据！！！
# import pandas as pd
# df=pd.read_csv("Os_GObottom10%1.csv")
# df01=df.groupby("GO_term").apply(lambda x:x["genename"].tolist())
# # print(df01)
# df01.to_csv("Os_GObottom10%1-1.csv")
# print(str(df01.values))
# print(df01.get_group("GO:0015074"))
# a=open("25.txt","r")
# for i in a:
#     i=i.strip()
#     print(df01.get_group(str(i)))
##################################################################
# import pandas as pd
# df=pd.read_csv("拟南芥翻译组数据.csv")
# df2=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.5,0.6,0.7,1])).count()
# df2=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.5,0.6,0.7,1])).mean()
# df2=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.5,0.6,0.7,1])).mean()
# df2=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.5,0.6,0.7,1])).std()
# df2=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.5,0.6,0.7,1])).sem()
# df2=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.35,0.38,0.41,0.44,0.47,0.5,1])).count()
# # df3=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.3,0.35,0.4,0.45,0.5,0.6,1])).mean()
# df4=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.35,0.37,0.39,0.41,0.43,0.45,0.5,1])).mean()
# print(df2)
##################################################################
# import pandas as pd
# df=pd.read_csv("水稻翻译组数据.csv")
# # df2=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.4,0.45,0.5,1])).count()
# df2=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.4,0.45,0.5,1])).mean()
# df2=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.4,0.45,0.5,1])).mean()
# df2=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.4,0.45,0.5,1])).std()
# df2=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.4,0.45,0.5,1])).sem()


# # df2=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.35,0.38,0.41,0.44,0.47,0.5,1])).count()
# # # df3=df.conservation.groupby(pd.cut(df.conservation,bins=[0,0.3,0.35,0.4,0.45,0.5,0.6,1])).mean()
# # df4=df.TE.groupby(pd.cut(df.conservation,bins=[0,0.35,0.37,0.39,0.41,0.43,0.45,0.5,1])).mean()
# print(df2)
##############################################################################
# import pandas as pd
# df=pd.read_csv("At_GOtop10%1.csv")
# df01=df.groupby("GO_term").apply(lambda x:x["genename"].tolist())
# # print(df01)
# df01.to_csv("At_GOtop10%1-1.csv")
###################
# import pandas as pd
# df=pd.read_csv("At_GObottom10%1.csv")
# df01=df.groupby("GO_term").apply(lambda x:x["genename"].tolist())
# # print(df01)
# df01.to_csv("At_GObottom10%1-1.csv")
###################
# import pandas as pd
# df=pd.read_csv("Os_GOtop10%1.csv")
# df01=df.groupby("GO_term").apply(lambda x:x["genename"].tolist())
# # print(df01)
# df01.to_csv("Os_GOtop10%1-1.csv")
###################
# import pandas as pd
# df=pd.read_csv("Os_GObottom10%1.csv")
# df01=df.groupby("GO_term").apply(lambda x:x["genename"].tolist())
# # print(df01)
# df01.to_csv("Os_GObottom10%1-1.csv")
############################################################################
# import pandas as pd
# df=pd.read_csv("十字花科-禾本科不同结构类型.csv")
# df01=df.number.groupby(df.type).sum()
# print(df01)
###########################################################################
# import pandas as pd
# df=pd.read_csv("十字花科stem位置分布.csv")
# df2=df.location.groupby(pd.cut(df.location,bins=[0,10,20,30,40,50,60,70,80,90,100])).count()
# print(df2)

# df=pd.read_csv("禾本科stem位置分布.csv")
# df2=df.location.groupby(pd.cut(df.location,bins=[0,10,20,30,40,50,60,70,80,90,100])).count()
# print(df2)

# import pandas as pd
# df=pd.read_csv("十字花科segment位置分布.csv")
# df2=df.location.groupby(pd.cut(df.location,bins=[0,10,20,30,40,50,60,70,80,90,100])).count()
# print(df2)
# import pandas as pd
# df=pd.read_csv("禾本科segment位置分布.csv")
# df2=df.location.groupby(pd.cut(df.location,bins=[0,10,20,30,40,50,60,70,80,90,100])).count()
# print(df2)
########################################################################
import pandas as pd
# df=pd.read_csv("十字花科hairpin5-3closing-pair.csv")
# df01=pd.pivot(df,index="x",columns="y",values="number")
# df01.to_csv("十字花科hairpin5-3closing-pair-1.csv")

# df=pd.read_csv("禾本科hairpin5-3closing-pair.csv")
# df02=pd.pivot(df,index="x",columns="y",values="number")
# df02.to_csv("禾本科hairpin5-3closing-pair-1.csv")

# df=pd.read_csv("十字花科hairpin5-3mismatch.csv")
# df03=pd.pivot(df,index="x",columns="y",values="number")
# df03.to_csv("十字花科hairpin5-3mismatch-1.csv")

# df=pd.read_csv("禾本科hairpin5-3mismatch.csv")
# df04=pd.pivot(df,index="x",columns="y",values="number")
# df04.to_csv("禾本科hairpin5-3mismatch-1.csv")

# df=pd.read_csv("十字花科internal loops5-3mismatch.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科internal loops5-3mismatch-1.csv")

# df=pd.read_csv("禾本科internal loops5-3mismatch.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科internal loops5-3mismatch-1.csv")

# df=pd.read_csv("十字花科internal loops5-3closing pair.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科internal loops5-3closing pair-1.csv")

# df=pd.read_csv("禾本科internal loops5-3closing pair.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科internal loops5-3closing pair-1.csv")

# df=pd.read_csv("十字花科internal loops5-3length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科internal loops5-3length-1.csv")
#
# df=pd.read_csv("禾本科internal loops5-3length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科internal loops5-3length-1.csv")

# df=pd.read_csv("十字花科internal loops5-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科internal loops5-closing pair-length-1.csv")

# df=pd.read_csv("禾本科internal loops5-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科internal loops5-closing pair-length-1.csv")

# df=pd.read_csv("十字花科internal loops3-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科internal loops3closing pair-length-1.csv")

# df=pd.read_csv("禾本科internal loops3-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科internal loops3closing pair-length-1.csv")

# df=pd.read_csv("十字花科bulge loops5-3closing pair.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科bulge loops5-3closing pair-1.csv")

# df=pd.read_csv("禾本科bulge loops5-3closing pair.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科bulge loops5-3closing pair-1.csv")

# df=pd.read_csv("十字花科bulge5-3mismatch.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科bulge5-3mismatch-1.csv")
##################
# df=pd.read_csv("十字花科bulge5-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科bulge5-closing pair-length-1.csv")

# df=pd.read_csv("十字花科bulge3-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科bulge3-closing pair-length-1.csv")
#
# df=pd.read_csv("禾本科bulge5-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科bulge5-closing pair-length-1.csv")

# df=pd.read_csv("禾本科bulge3-closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科bulge3-closing pair-length-1.csv")
#
# df=pd.read_csv("十字花科multi loops5-3closing pair.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科multi loops5-3closing pair-1.csv")

# df=pd.read_csv("禾本科multi loops5-3closing pair.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科multi loops5-3closing pair-1.csv")

# df=pd.read_csv("十字花科multi loops5-3mismatch.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科multi loops5-3mismatch-1.csv")

# df=pd.read_csv("禾本科multi loops5-3mismatch.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科multi loops5-3mismatch-1.csv")

# df=pd.read_csv("禾本科multi loops5-3closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科multi loops5-3closing pair-length-1.csv")

# df=pd.read_csv("十字花科multi loops5-3closing pair-length.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科multi loops5-3closing pair-length-1.csv")

# df=pd.read_csv("十字花科multi loops-branch长度-个数.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("十字花科multi loops-branch长度-个数-1.csv")

# df=pd.read_csv("禾本科multi loops-branch长度-个数.csv")
# df=pd.pivot(df,index="x",columns="y",values="number")
# df.to_csv("禾本科multi loops-branch长度-个数-1.csv")