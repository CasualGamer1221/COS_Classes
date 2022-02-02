# Task 1

quote = "The-only-way-to-learn-a-new-programming-language-is-by-writing-programs-in-it."

print(quote[9:12])
print (quote[0:len(quote)//2])
print (quote[0:(len(quote)//2)-16])


quote2=''
for i in range(len(quote)):
    if i%2==0:
        quote2+=quote[i]
print (quote2)


counter =10
while counter > 0:
    print(quote[quote.find('.')])
    counter-=1

