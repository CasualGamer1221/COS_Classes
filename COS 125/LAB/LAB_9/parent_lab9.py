#Task 1
lab9file=open("lab9_data.txt")
for line in lab9file:
    print (line.split()[1])

#Task 2
lab9file=open("lab9_data.txt")
sum=0
for line in lab9file:
    sum+= int(line.split()[2])
print ("Sum of all salaries: ",sum)

#Task 3
lab9file=open("lab9_data.txt")
datalist=[]
for line in lab9file:
    datalist.append(line.split())
for i in range(len(datalist)):
    datalist[i][2]=((int(datalist[i][2])*1.1)//1)



f= open("lab9_updated.txt" , "a")
for i in datalist:
    f.write(str(i))