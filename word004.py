import win32com.client as wc
from docx import Document
import os
# path="B:\\Lost\\P1\\A10（教育局代发）县（区）域义务教育发展状况调查"
# files=os.listdir(path)
# filenames=[]
# for file in files:
#     if file.endswith(".doc"):
#         filenames.append(file)
#
# word=wc.Dispatch("Word.Application")
# for file in filenames:
#     filepath=path+"\\"+file
#     namenew=path+"\\"+file+"x"
#     doc=word.Documents.Open(r"B:\\Lost\\P1\\A10（教育局代发）县（区）域义务教育发展状况调查\\"+file)
#     # doc.SaveAs(r"B:\\Lost\\P1\\A10（教育局代发）县（区）域义务教育发展状况调查"+file+"x",12,False,"",True,"",False,)
#     doc.SaveAs(r"B:\\Lost\\P1\\aaa\\"+file+"x",12)
# doc.Close
# word.Quit

path="B:\\Lost\\P1\\aaa"
files=os.listdir(path)
filenamesdocx=[]
for file in files:
    if file[0]!="~":
        if file.endswith(".docx"):
            filenamesdocx.append(file)
all=[]
类别1=[]
数量1=[]
类别2=[]
数量2=[]
for filename in filenamesdocx:
    doc=Document(filename)
    tb1=doc.tables[0]
    row=tb1.rows
    for r in tb1.rows:
        row_cells=r.cells
        类1=row_cells[0].text
        类2=row_cells[2].text
        数1=row_cells[1].text
        数2=row_cells[3].text
        数量1.append(数1)
        数量2.append(数2)
        类别1.append(类1)
        类别2.append(类2)

result=open("a2.xlsx","w",encoding='gbk')
# for m in range(10)：
result.write(str(数量1))
# result.close()