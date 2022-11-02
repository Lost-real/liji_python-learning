#
import pandas as pd
df=pd.read_csv("team.csv")
df1=pd.read_csv("At5utr200bp6braTE14492t_test检验1.csv")
df01=df.set_index("name").groupby("team").groups
df02=df.filter(items=["Q1","Q2","Q3","Q4"])
df03=df.Q1[lambda s:max(s.index)]
df04=df.sort_index(ascending=False)
df05=df.sort_index(axis=1,ascending=False)
df06=df.team.map({"A":"一班","B":"二班","C":"三班","D":"四班"})
# print(df.team.map({"A":"一班","B":"二班","C":"三班","D":"四班"}))
df07=df.team.map("I am a".format)
df08=df.groupby("team").agg(max)
df09=df.agg(["sum","min"])
df10=df.groupby(lambda x:x>=50).sum()
df13=df.groupby('team').transform(max) # 最大值
# Q1成绩至少有一个大于97的组
df.groupby(['team']).filter(lambda x: (x['Q1'] > 97).any())
# 所有成员平均成绩大于60的组
df14=df.groupby(['team']).filter(lambda x: (x.mean() >= 60).all())
# Q1所有成员成绩之和超过1060的组
df15=df.groupby('team').filter(lambda g: g.Q1.sum() > 1060)
# 所有列使用一个计算方法
# 指定列名，列表是为原列和方法
df16=df.groupby('team').Q1.agg(Mean='mean', Sum='sum')
df17=df.groupby('team').agg(Mean=('Q1', 'mean'), Sum=('Q2', 'sum'))
df18=df.groupby('team').agg(
    Q1_max=pd.NamedAgg(column='Q1', aggfunc='max'),
    Q2_min=pd.NamedAgg(column='Q2', aggfunc='min')
)
# 聚合结果使用函数
# lambda/函数，所有方法都可以用
def max_min(x):
    return x.max() - x.min()
# 定义函数
df19=df.groupby('team').Q1.agg(Mean='mean',
                          Sum='sum',
                          Diff=lambda x: x.max() - x.min(),
                          Max_min=max_min
                         )

idx = pd.date_range('1/1/2020', periods=100, freq='T')
df2 = pd.DataFrame(data={'a':[0, 1]*50, 'b':1},
                   index=idx)

# 每20分钟聚合一次
df201=df2.groupby('a').resample('20T').sum()
# 三个周期一聚合（一分钟一个周期）
df202=df2.groupby('a').resample('3T').sum()
# 30秒一分组
df203=df2.groupby('a').resample('30S').sum()
# 每月
df204=df2.groupby('a').resample('M').sum()
# 以右边时间点为标识
df205=df2.groupby('a').resample('3T', closed='right').sum()

# 将Q1成绩换60分及以上、60分以下进行分类
df20=pd.cut(df.Q1, bins=[0, 60, 100])

# Series使用
df21=df.Q1.groupby(pd.cut(df.Q1, bins=[0, 60, 100])).mean()
print(df21)

# DataFrame使用
df.groupby(pd.cut(df.Q1, bins=[0, 60, 100])).count()



# 各组Q1（为参数）成绩最高的前三个
# def first_3(df_, c):
#     return df_[c].sort_values(ascending=False).head(3)
# 调用函数
# df11=df.set_index('name').groupby('team').apply(first_3, 'Q1')
# print(df11)
# 通过设置group_keys，可以使分组字段不作为索引

# (
#     df.groupby('team')
#     .apply(lambda x: pd.Series({
#         'Q1_sum'       : x['Q1'].sum(),
#         'Q1_max'       : x['Q1'].max(),
#         'Q2_mean'      : x['Q2'].mean(),
#         'Q4_prodsum'   : (x['Q4'] * x['Q4']).sum()
#     }))
# )

# 定义一个函数
# def f_mi(x):
#         d = []
#         d.append(x['Q1'].sum())
#         d.append(x['Q2'].max())
#         d.append(x['Q3'].mean())
#         d.append((x['Q4'] * x['Q4']).sum())
#         return pd.Series(d, index=[['Q1', 'Q2', 'Q3', 'Q4'],
#                                    ['sum', 'max', 'mean', 'prodsum']])
# 使用函数
# df12=df.groupby("team").groups
# df12=df.groupby('team').apply(f_mi)
# print(df13)



# df.groupby('team').transform(np.std) # 标准差
# # 使用函数，和上一个学生的差值（没有处理姓名列）
# df.groupby('team').transform(lambda x: x.shift(-1))
# # 函数
# def score(gb):
#     return (gb - gb.mean()) / gb.std()*10
# # 调用
# grouped.transform(score)
# print(df10)
# print(df.assign(tag=(df.Q1>df.Q2).astype(int)))
# print(df.assign(Q7=lambda d:d.Q1*9/5+32))

#及格不及格感觉挺实用的
# print(df.assign(tag=(df.Q1>60).map({True:"及格",False:"不及格"})))
# print(df05.iloc[0,0])
# print(df.infer_objects().dtypes)
# print(df.astype({"Q1":"int32","Q2":"int32"}).dtypes)


# print(type(df02))
# print(df03)
