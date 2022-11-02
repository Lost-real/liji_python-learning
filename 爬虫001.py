#正则表达式练习
# import re
# example_text='我是kingname,我的微博账号是:kingname,密码是:12345678,QQ账号是:9999,密码是:890abcd,银行卡账号是:00001'
# # new_pattern=re.compile('账号是:(.*?),密码是:(.*?),',re.S)
# # user_pass=re.findall(new_pattern,example_text)
# new_pattern=('账号是:(.*?),密码是:(.*?),')
# user_pass=re.findall(new_pattern,example_text)
# print(user_pass)

#############
#先抓大后抓小的操作：
# import re
#
# big_small_text='''
# 有效用户：
# 姓名：张三
# 姓名：李四
# 无效用户：
# 姓名：二狗
# '''
# user_big=re.findall('有效用户：(.*?)无效用户',big_small_text,re.S)
# print('user_big的值为：{}'.format(user_big))
# user_useful=re.findall('姓名：(.*?)\n',user_big[0])
# print('真正有效的人名：{}'.format(user_useful))

##############
#括号内外的差异
#我们匹配到的数据都是括号里面的数据，切记一定是括号里面的数据
# import re
# html='''
# <div class="tail-info">客户端</div>
# <div class="tail-info">2017-01-01 13:45:00</ div>
# '''
# result1_1=re.findall('tail-info">(.*?)<',html)
# result1_2=re.findall('tail-info">2017(.*?)<',html)
# result1_3=re.findall('tail-info">(2017.*?)<',html)
# print(result1_1)
# print(result1_2)
# print(result1_3)

################################
with open('110.txt') as f1:
    a=f1.readlines()
    b=f1.read()
    print(a)
    # print(b)