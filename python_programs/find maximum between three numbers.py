#2.	Write a C program to find maximum between three numbers.

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))

if num1>num2:
    if num1>num3:
        print("num1 is max, num1: ",num1)
    else:
        print("num3 is max, num3: ", num3)
elif num2>num3:
    print("num2 is max, num2: ", num2)
else:
    print("num3 is max, num3: ",num3)
