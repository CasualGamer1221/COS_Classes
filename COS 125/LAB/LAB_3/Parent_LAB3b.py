listB = ["cat", "dog", "bunny", "squirrel", "bear", "pig"]
listC = [2, 5, 99, 3, 101, -99, 0, 4]

#Task2a
for i in range(2,101,2):
    print("",i,"",end='')
print()
    
#Task2b
for i in range(len(listB)):
    print("",i,"", end='')
    print("",listB[i])
print()

for w in listB:
    print("",w,"", end='')
print()


#Task2c
max_value=int()
for n in listC:
    if n > max_value:
        max_value=n
print("",max_value,", ", end='')
print("index", n)
print()

    
