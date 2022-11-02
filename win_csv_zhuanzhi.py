import pandas as pd
df=pd.read_csv("Os3utr300bp10539out1merge1sortedreplacefillupcut300bp.csv")
df1=df.T
# print(df.T)
df1.to_csv("Os3utr300bp10539out1merge1sortedreplacefillupcut300bpzhuanzhi.csv",header=None)