#python正则表达式学习20220710
#参考网站：https://blog.csdn.net/weixin_42414714/article/details/108514649
import re

#每个普通字符匹配其对应的字符
# a1=re.findall('abcde',"abcdefabcd")
# print(a1)

#匹配中文
# a2=re.findall('李季',"李季立即李季")
# print(a2)

#元字符|
#匹配规则: 匹配 | 两侧任意的正则表达式即可
# a3=re.findall('com|cn',"www.baidu.com/www.tmooc.cn")
# print(a3)

#元字符。
#匹配除换行符外的任意一个字符
# a4=re.findall('张.丰',"张三丰,张四丰,张五丰,张丰")
# print(a4)

#元字符：[字符集]
#匹配规则：匹配字符集中的任意一个字符
#表达形式：
# a5=re.findall('[aeiou]',"How are you")
# print(a5)

#匹配字符集反集
#元字符：[^字符集]
#匹配规则：匹配除了字符集以外的任意一个字符
# a6=re.findall('[^0-9]',"Use 007 port")
# print(a6)

#匹配字符串开始位置
#元字符：……
#匹配目标字符的开始位置
# a7=re.findall('^Jame',"Jame,hello")
# print(a7)

# #匹配字符串结束的位置
# 元字符：$
# 匹配规则：匹配目标字符串的结束位置
# a8=re.findall('Jame$',"Hi,Jame")
# print(a8)

#元字符：*
#匹配规则：匹配前面的字符出现0次或者多次
# a9=re.findall('wo*',"wooooo~~w!")
# print(a9)

#元字符+
#匹配规则：匹配前面的字符出现1次或者多次
# a10=re.findall('[A-Z][a-z]+',"Hello World")
# print(a10)

#元字符：？
#匹配规则：匹配前面的字符出现0次或者1次，其实，？可以理解为"有"和"无"
# a11=re.findall('-?[0-9]+',"Jame,age:18,-26")
# print(a11)

# 元字符：{n}
# 匹配规则：匹配前面的字符出现n次
# a12=re.findall('1[0-9]{10}',"Jame:13886495728")
# print(a12)

#元字符：{m,n}
#匹配字符：匹配前面的字符出现m-n次
# a13=re.findall('[1-9][0-9]{5,10}',"Baron:1259296994")
# print(a13)

#自己练习用
# b1=re.findall('GGG.{2}GGG',"GGGAGGGTTTTCCCCGGGAAGGGTTTT")
# print(b1)

#匹配任意数字符号和非数字符号
#匹配规则：\d匹配任意数字字符；\D匹配任意非数字字符
# a14=re.findall('\d{1,5}',"Mysql:3306,http:80")
# print(a14)



# 匹配任意普通字符，非普通字符
# 元字符：\w \W
# 匹配规则：\w匹配普通字符(数字，字母，下划线，汉字)；\W匹配非普通字符(b)
# a14=re.findall('\w+',"server_port=8888-")
# print(a14)

#匹配任意空字符
# 元字符：\s \S
# 匹配规则：\s匹配空字符，\S匹配非空字符
# 说明：空字符指的是空格 \r \n \t \v \f字符
# a15=re.findall('\w+\s+\w+',"hello world")
# print(a15)

#匹配单词和非单词的边界位置
# 元字符：\b \B
# 匹配规则：\b表示单词边界；\B非单词边界
# 说明：单词边界指数字，字母，汉字，下划线与其他字符交界的位置
# a16=re.findall(r'\bis\b',"this is a test.")
# print(a16)


#总结：
#匹配字符：。 [...] [^...] \d \D \w \W \s \S
#匹配重复： * + ？ {n} {m,n}
#匹配位置： ^ $ \A \Z \b \B
