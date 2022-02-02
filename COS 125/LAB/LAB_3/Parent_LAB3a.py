
#Task 1a
x=0
while x<100:
    if x%2 != 0:
        print("",x,"", end='')
    x+=1
print()
#Task 1b

numa=int(input("Give first number"))
numb=int(input("Give second number"))

while numa!=0:
    numa-=1
    print("outer")
    while numb!=0:
        print ("inner")
        numb-=1
print()
    
#Task 1c

exitletter=""
exitword=""
while exitletter!="q":
    exitletter=input("Enter a character:",)
    print("outer")
    while exitword!="quit":
        exitword=input("enter a word:",)
        print("inner")