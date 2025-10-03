choice='y'
while choice !='n':
    marks = int(input("enter marks : "))
    if marks>=91 and marks<=100:
        print("A")
    elif marks>=71 and marks<=90:
        print("B")
    elif marks>=51 and marks<=70:
        print("C")
    elif marks>=35 and marks<=50:
        print("D")
    elif marks>=0 and marks<=34:
        print("F")
    else:
        print("Invalid input") 
    choice = input("Do u want to continue ? y or n")