import re

k = re.match("a","aheallo")
k = re.search("al","healloa")
k = re.findall("a","aheallo")
k = re.finditer("a","ahealloa")
for i in k:
    print(i)