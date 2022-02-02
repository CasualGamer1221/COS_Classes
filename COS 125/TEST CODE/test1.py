number= int(input("enter a number"))
if number % 2 == 0 :
    if number >= 0:
        number += 1
        for i in range(0,number):
            print(i)
        number=0
    if number < 0:
        number -=1
        for i in range(0,number,-1):
            print(i)
        number=0
number=int(input("enter a number"))
