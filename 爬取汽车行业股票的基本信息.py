import requests
import re
html_str = requests.get("http://www.cankaoxiaoxi.com/finance/20221006/2492174.shtml").content.decode()
# print(html_str)
# title=re.search('title>(.*?)<',html_str,re.S).group(1)
# print(f"页面标题为：{title}")

content_list=re.findall("<p>(.*?)<",html_str,re.S)
content_str="\n".join(content_list)
print(content_str)