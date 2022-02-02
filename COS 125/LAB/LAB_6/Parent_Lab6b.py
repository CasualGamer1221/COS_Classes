#Task 2

rossum = [
    'don\'t', 'you', 'hate', 'code', 'that\'s', 'not', 
    'properly', 'indented?', 'making', 'it', 'part', 
    'of', 'the', 'syntax', 'guarantees', 'that', 
    'all', 'code', 'is', 'properly', 'indented.'
]

rossum.append('Guido')
rossum.append('Rossum')
rossum.remove('hate')
for x in rossum:
    if x == 'properly':
        rossum.remove('properly')

rossum2=[rossum[6:]]
#print(rossum,rossum2)      #PRINTS LIST ROSSUM AND ROSSUM2 ---for testing!

rossum3=rossum[2:]
#print(rossum3)

rossum4=rossum3
rossum4.remove('syntax')
#print(rossum4)

rossum5=[rossum3 + rossum4]
print (rossum5)








