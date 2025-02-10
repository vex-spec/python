# program to check wether a number is a prime number or not
from operator import truediv

number = float(input("enter the number"))
if number ==0 or number ==1 :
    print(number,"is not a prime number")
elif number >1 :
    for i in range (2,number):
        if (number % i) ==0:
            print(number,"is not prime")
            print(i,"times", number//i ,"is",number)
            break
    else:
        print(number,"is a prime")

else :
    print(number, "is not prime")