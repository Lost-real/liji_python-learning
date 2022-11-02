"""将多行文件转换为一行
例：
>001
AAGTCCGGTAA
GGCTAGCTAAC
TTCGAACGACA
>002
GGCTAGCATGA
CACATCGACAC
CAGTAGCATCT
转换为：
>001
AAGTCCGGTAAGGCTAGCTAACTTCGAACGACA
>002
GGCTAGCATGACACATCGACACCAGTAGCATCT
"""
fr=open('ztotgen31spAT1G01550.2.txt', 'r')
fw=open('ztotgen31spAT1G01550.2-1.txt', 'w')
seq={}
for line in fr:
    if line.startswith('>'):    #判断字符串是否以‘>开始’
        name=line.split()[0]    #以空格为分隔符，并取序列为0的项。
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')
fr.close()
# print(seq)
for i in seq.keys():
    fw.write(i+"\n")
    # fw.write('\n')
    fw.write(seq[i]+"\n")
    # fw.write('\n')
fr.close()