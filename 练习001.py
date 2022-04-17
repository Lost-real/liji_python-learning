list1 =[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9,7,6]
# print(list1)
a1 = [i for i in range(len(list1))]
# print(a1)
a2 = [i for i in list1]
a3 = dict(zip(a1, a2))
# print(a3)
b = []
n=5
while n<=9:
    for i in range(len(list1)):
        c = list1[i:i + n]
        # print(c)
        d = 0
        if len(c) == n:
            for j in c:
                d += int(a3.get(j, 100))
            b.append(d)
        else:
            pass
    n+=1
# print(b)