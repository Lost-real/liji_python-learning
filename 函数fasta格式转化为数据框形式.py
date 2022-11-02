# def format_for_heatmap(b):
b=open("31.txt","r")
def convertformat(a):
    newlist1=[]
    seq = {}
    # 下面的这个for循环其实就是一个生成字典的过程，需要仔细品味，领悟
    for line in a:
        if line.startswith('>'):  # 判断字符串是否以">"开始
            name = line.strip().split('>')[1]  # 以>为分隔符，并取序列为1的项,也就是不带有>的，基因的名字
            # name=line.strip().split()[0]    #以空格为分隔符，并取序列为0的项，也就是带有>的基因的名字
            seq[name] = ''
        else:
            seq[name] += line.replace('\n','')  # str.replace(old, new[, max]);old -- 将被替换的子字符串;new -- 新字符串，用于替换old子字符串;max -- 可选字符串, 替换不超过 max 次



    for i in seq.keys():
        # print(i + "\t" + seq[i])
        newlist1.append(i+"    "+seq[i]+"\n")
    # return ("\t".join(newlist1))
    return ("".join(newlist1))
c=convertformat(b)
print(c)