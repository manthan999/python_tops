# l = [1,2,34,5,6,7,9,9,10,11]

# k = iter(l)

# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))



def square(a):
    for i in range(a):
       yield i*i

k = iter(square(10))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
