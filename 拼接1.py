import json

with open("brassiceae3.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
data_1 = open("brassiceae3奇数行.txt", 'w', encoding='utf-8')
data_2 = open("brassiceae3偶数行.txt", 'w', encoding='utf-8')

num = 0  # 行数-1
for line in lines:
    if (num % 2) == 0:  # num为偶数说明是奇数行
        print(line.strip(), file=data_1)  # .strip用来删除空行
    else:  # # num为奇数说明是偶数行
        print(line.strip(), file=data_2)
    num += 1

data_1.close()
data_2.close()