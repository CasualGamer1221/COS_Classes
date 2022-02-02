#Task 2A
def isNegative(num):
    if num < 0:
        return True
    else:
        return False
isNegative(float(input("enter a number: ")))


#Task2B
def multiplyList(alist,num):
    for i in alist:
        alist[i]=alist[i]*num

list1=[1,2,3]
numb=int(input("Enter a number: "))
print(multiplyList(list1,numb))
 

#Task2C
def loopOnPositive():
    number=()
    if isNegative == False:
        float(input("Enter a number: "))
        print(number*.5)