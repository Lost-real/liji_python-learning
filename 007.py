
import os

from docx import Document

path = "E:\\pythonworking\\file\\aa2"

files = os.listdir(path)
filenamedocx=[]

for file in files:
  if file[0] != "~":

    if file.endswith(".docx"):
      filenamedocx.append(file)
# print(filenamedocx)
nameall=[]
for f in filenamedocx:
  # print(f)
  d=Document(f)
  t=d.tables[0]
  row=t.rows
  # # print(row)
  for i in row:
    row_cells=i.cells
    name=row_cells[1].text
    nameall.append(name)
  #   print(name)
result = open('resultdata.xls', 'w', encoding='gbk')
for m in range(len(nameall)):
    result.write(str(nameall[m]))
    result.write('\t')