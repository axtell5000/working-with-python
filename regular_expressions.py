import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern2 = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
string = "axtell.stephen@gmail.com"
string2 = "abcdefg4"
a = pattern.search(string)
d = pattern2.search(string2)
b = pattern.findall(string)
c = pattern.fullmatch(string)
print(a)
print(b)
print(c)
print(d)
# Exercise password regex
