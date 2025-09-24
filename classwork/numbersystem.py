#  decimal -> octal
# number=158
# sum=0
# i=1
# while number>0:
#     rem=number%8
#     sum=sum+(rem*i)
#     print(rem)
#     number//=8
#     i*=10
# print(sum)

#  decimal to hexadecimal
# number=155
# sum=""
# arr=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
# while number>0:
#     rem=number%16
#     sum = str(arr[rem])+sum
#     print(rem)
#     number//=16

# print(sum)

# binary to decimal
# number=1110100
# sum=0
# i=0
# while number>0:
#     rem=number%10
#     sum+=rem*pow(2,i)
#     number//=10
#     i+=1
# print(sum)

# binary to octal
# binary -> decimal -> octal ---------------------
# binary -> decimal:-
number=1110100
sum=0; i=0
while number>0:
    rem=number%10
    sum+=rem*pow(2,i)
    number//=10
    i+=1
print(sum)
# decimal -> octal
s=0; i=1
while sum>0:
    rem=sum%8
    s= s + (rem*i)
    sum//=8
    i*=10
print(s)