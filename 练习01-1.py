a=open('zoutbrassicaceae_AT5G60390.3-2.txt', 'r')
b=open('zoutbrassicaceae_AT5G60390.3-3.txt', 'w')
seq={}
#下面的这个for循环其实就是一个生成字典的过程，需要仔细品味，领悟
for line in a:
    if line.startswith('>'):    #判断字符串是否以‘>开始’
        name=line.strip().split('>')[1]    #以空格为分隔符，并取序列为0的项。
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')#str.replace(old, new[, max]);old -- 将被替换的子字符串;new -- 新字符串，用于替换old子字符串;max -- 可选字符串, 替换不超过 max 次
# print(seq.values())
# print(seq.keys())
# a.close()

for i in seq.keys():
    print(i+"\t"+seq[i][800:2000])
    b.write(i+"\t"+seq[i][800:2000]+"\n")#注意windows上面需要用加上"\n",当在linux上运行时，不用加"\n"
    # fw.write('\n')
    # b.write(seq[i]+"\n")
    # fw.write('\n')
# f.close()