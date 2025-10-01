# s = {100,20,30,40,50,60,70,70,1,True,0,False}
# s.add(1000)
# s.remove(10000)
# s.discard(10000)
# s.pop()
# print(s)

# if 10 in s:
#     print(10)

# for i in s:
#     print(i)



# a = {10,20,30,40,50}
# b = {30,40,50,60,70}

# a.update(b)
# c = a.union(b)

# c = a.intersection(b)
# a.intersection_update(b)
# c  = a & b


# c = a.difference(b)
# a.difference_update(b)



# c  =a.symmetric_difference(b)
# a.symmetric_difference_update(b)
# print(a)

# a.union(b)
# c = a.intersection(b)
# print(c)


# x  =frozenset({10,20,30})

x = {10,20,30,40,50}
y  ={100,200}

print(x.issuperset(y))
print(y.issubset(x))
print(x.isdisjoint(y))