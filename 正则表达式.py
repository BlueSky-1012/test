import re

msg = "aaabbbcccddd"

pattern = re.compile("bbb")
result = pattern.match(msg)  # 没有匹配
print(result)

# 使用正则模块的 re 方法：match
msg = "aaabbbcccddd"
print(re.match("aaa", msg))  # 从开头开始匹配，头必须满足正则表达式（遇到第一次匹配不成功就返回None）

result = re.search("bbb", msg)  # 从头匹配到结尾，匹配整个字符串
print(result)
print(result.span())  # 返回位置
print(result.group())  # 返回匹配的结果
print(result.groups())  # 返回匹配的结果

s = "哈哈哈2a"
result = re.search("[123][a-z]", s)
print(result)

msg = "abcd7vjkjgds3dgs00dsagd"
result = re.search("[a-z][0-9][a-z]", msg)
print(result)

result = re.findall("[a-z][0-9][a-z]", msg)
print(result)

# a3a s33a a234a
msg = "abcd7vjk896jgds3dgs00dsagd"
result = re.findall("[a-z][0-9]+[a-z]", msg)
print(result)

# qq 号码验证 5-11 位，开头不能是 0
msg = "1324613242"
result = re.match("^[1-9][0-9]{4,10}$", msg)
print(result)

# 用户名可以是字母或者数字，不能是数字开头，用户名长度必须6位以上
msg = "ad4adming"
result = re.search("^[a-zA-Z][0-9a-zA-Z]{5,}$", msg)
print(result)
