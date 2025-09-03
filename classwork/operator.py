# Arithmetic Operators

a = input("Enter first number: ")
b = input("Enter second number: ")
print("Addition:", int(a) + int(b))
print("Subtraction:", int(a) - int(b))
print("Multiplication:", int(a) * int(b))
print("Division:", int(a) / int(b))
print("Floor Division:", int(a) // int(b))
print("Modulus:", int(a) % int(b))
print("Exponentiation:", int(a) ** int(b))

# Assignment Operators
a = 10
b = 20
c = a
print(a)
a += b
print(a)
a -= b      
print(a)
a *= b  
print(a)
a /= b
print(a)        
a //= b
print(a)
a %= b
print(a)
a **= b
print(a)


# Comparison Operators

a = 10
b = 20
print(a == b)   
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# membership Operators

a ="hello world"
print("hello" in a)
print("hello" not in a)
print("world" in a)
print("world" not in a)
print("python" in a)

# Identity Operators

a = 10
b = 20
print(a is b)
print(a is not b)   
c = a
print(a is c)