# student = {
#     "name":"Meet",
#     "email":"meet@gmail.com",
#     "sub": ["java","Python","Php"]
# }

# print(student)
# print(student['name1'])
# print(student.get('name1'))

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student['sub'][1])

# student['name1'] = 'Krish'
# student.update({"age":56,"phone":7485968587})
# student.pop()
# student.popitem() 

# del student['name']
# del student
# student.clear()
# print(student)


# for i in student.keys():
#     print(i)

# for i in student.values():
#     print(i)

# for i,j in student.items():
#     print(i,j)


products = {
    "Laptop" :{
        "price":30000,
        "qty":10
    },
     "Mouse" :{
        "price":300,
        "qty":15
    },
     "Keyboard" :{
        "price":3000,
        "qty":11
    },

}

for i,j in products.items():
    print(i)
    for x,y in j.items():
        print(x,y)