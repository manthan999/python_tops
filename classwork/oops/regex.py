import re

# k = re.match("a","aheallo")
# k = re.search("al","healloa")
# k = re.findall("a","aheallo")
# k = re.finditer("a","ahealloa")
# for i in k:
#     print(i)

# k = re.sub("a",'X',"aheallo")
# print(k)

# k = re.split("o","Hello python hello java")
# print(k)


# k = re.findall("a.b","axbhhghgavbhg")
# print(k)

# k = re.match("^Hello","Hello abc")
# k = re.search("abc$","Hello abc")

# k = re.search("la*l","Helaaaalo abc")

# k = re.search("H+e","Hello abc")
# k = re.search("Helll?o","Hello abc")
# k = re.findall("[aeiou]","Hello")

# k = re.findall(r"hello\b","hello hellooo erhello")
# print(k)

# name = "testeeeeee"
# k = re.match("^[a-z]{5,10}$",name)
# if k is None:
#     print("Invalid name")
# else:
#     print("valid name")

email = "tops@gmail.com"

k = re.match("^[a-z0-9A-Z-_]+@[a-zA-Z]+\\.[a-zA-Z]{2,4}$",email)
if k is None:
    print("Invalid email")
else:
    print("Valid email")