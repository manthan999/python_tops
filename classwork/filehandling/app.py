# f = open("test.txt",'w')
# # f.write("Hello python")
# f.writelines(["Hello java","Hello Tops"])
# f.close()


# f = open("test.txt",'a')
# f.write("Hello python")
# f.close()

# f = open("test.txt",'r')
# data = f.read()
# data = f.readline()
# data1 = f.readline()
# data = f.readlines()
# print(data)


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'java' in data:
#         print(data)
#     if not data:
#         break


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'java' in data:
#         print(data)
#     if not data:
#         break

# f = open("test.txt",'r')
# data = f.readlines()
# k = filter(lambda x : 'java' in x.lower(), data)
# print(list(k))


# with open("test.txt") as f:
#     print(f.tell())
#     f.seek(4)
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open('D://hello.txt','w+') as f:
#     f.write("something...")
#     f.seek(0)
#     data = f.read()
#     print(data)

# d = {"name":"xyz","email":"xyz@gmail.com"}

import json
# with open("data.json",'w') as f :
#     json.dump(d,f)

try :
    with open("data.json",'r') as f :
        data = f.read()
        k = json.loads(data)
        for i in k:
            print(i['name'])
            for x in i['states']:
                print(x['name'])
            print("**********")
        f.close()
except Exception as e:
    print(e)

