

# def msg():
#     print("Hello python")

# def square(a):
#     print(a*a)

# def add(a,b):
#     print(a+b)

# def getmsg():

#     return "Hello"


# def mul(a,b):
#     return a*b

    
# msg()
# square(10)
# square(15)
# add(10,30)
# a = getmsg()
# print(a)
# print(getmsg())

# print(mul(10,20))
# print(add(10,20))


# def person(id=0,name="test",email="test@gmail.com"):
#     # print(id,name,email)
#     return id,name,email

# print(person(name="abc",email="abc@gmail.com"))

# def add(*a):
#     sum = 0
#     for i in a:
#         sum+=i
#     print(sum)
# add(10,20)

# def student(**a):
#     print(a)
# student(name="krish",email="krish@gmail.com")


# def square(a):
#     return a*a

# sq = lambda a:a*a
# add = lambda a,b : a+b

# print(sq(10))
# print(add(10,20))


# a = 10
# def test():
#     global a
#     a = 20
#     print(a)

# print("before : ",a)
# test()
# print("after : ", a)


# def square(a):
#     print(a*a)
#     a+=1
#     if a<25:
#         square(a)

# square(10)

# l = [1,2,3,4,5,6,7,8]
# # k = []

# # def square(a):
# #     return a*a

# # for i in l:
# #    j =  square(i)
# #    k.append(j)
# # k = map(square,l)

# k = map(lambda a:a*a,l)
# print(list(k))


# a = [10,20,30,40,50,60]
# b = [1,2,3,4,5]

# k = map(lambda x,y:x+y,a,b)
# print(list(k))


# l = [1,2,3,45,69,7,84,56,77,8]

# def checkodd(a):
#     if a%2!=0:
#         return a
    
# k = []
# for i in l:
#     j = checkodd(i)
#     if j is not None:
#         k.append(j)
# k = filter(lambda x : x%2!=0,l)
# print(list(k))

# subjects  = ["python",'java','node','android','sql']

# k = filter(lambda x : "a" in x ,subjects)
# print(list(k))

# # k = map(lambda x : len(x),subjects)
# x = list(k)
# print(x)
# m = map(lambda x : len(x),x)
# print(list(m))

# k = [1,2,3,4,5,6,7,8,9,10,16]