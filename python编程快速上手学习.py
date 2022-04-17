list1 =[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9,7,6]
# print(list1)
a1 = [i for i in range(len(list1))]
# print(a1)
a2 = [i for i in list1]
a3 = dict(zip(a1, a2))
# print(a3)
b = []
n=5
while n<=5:
    for i in range(len(list1)):
        c = a1[i:i+n]
        # print(c)
        d = 0
        if len(c) == n:
            for j in c:
                d +=a3.get(j, 100)
            d=d/n
            b.append(d)
        else:
            pass
    n+=1
print(b)
# def check_conserved_sequence(b):
m=0
for i in b:
    # b_pos = b.index(i)
    if i>=7.8:
        m+=1
        # print(a1[b_pos:b_pos+5])
        # print(a2[b_pos:b_pos+5])
    else:
        continue
print(m)
#     return m
# b=[1,23,34,45]
# a=check_conserved_sequence(b)
# print(a)

# max_value = max(b)
# max_pos = b.index(max_value)
# print(a1[max_pos:max_pos + 5])
# print(a2[max_pos:max_pos + 5])