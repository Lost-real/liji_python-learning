#一行代码实现excel拆分，并且新生成的excel以sheet name进行命名
# import office
# office.excel.sheet2excel(file_path='E://pythonworking/file/各个班级成绩.xlsx')
#参数作用：
# file_path = 将要拆分的Excel文件的位置，只能拆分xlsx后缀的Excel文件。

#####################
# 导入这个库：python-office，简写为office
# import office
#
# #1行代码，验证是否绑定成功
# office.excel.merge2excel(dir_path=r'E://pythonworking/file/excel合并/',output_file='test.xlsx')
#
# #参数作用：
# # dir_path = 文件夹的位置，建议把需要合并的多个excel文件放到同一个文件夹里。
# # output_file = 最终合并的excel文件放在哪里、叫什么名字，可以不填，默认是：merge2excel.xlsx

#####################################################
#pdf添加水印
import office  # 导入python-office

office.pdf.add_watermark() # 不需要对代码进行任何修改，直接运行


###########################################################
#word批量转pdf
# import office # 导入python-office
# #注意下面的path写法，很关键
# path = 'E:/pythonworking/file/word批量转pdf'  # path这里，填写你存放word文件的位置，例如：C:/app/workbook
# office.word.docx2pdf(path=path) # 程序就可以自动将该目录下的所有word文档，自动转换成pdf文档了