for i in range(100,1000):
    number = i
    temp = number
    sum = 0
    while number!=0:
        rem = number%10
        sum +=pow(rem,3)
        number = number//10
        
    if temp==sum:
        print(temp,"armstrong")
    else:
        # print(temp,"Not armstrong")
        pass