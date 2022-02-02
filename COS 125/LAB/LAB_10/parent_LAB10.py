#Task 1
import random as rand
def recsum(N):
    if N > 0:
        return N + recsum(N-1)
    else: return 0

print(recsum(10)) 

#Task 2
def boardcuts(L):
    if L > 0:
        return 1 + boardcuts(L - 4)
    else: return 0
        
print(boardcuts(40))

#Task 3
def recrev(List):
    if len(List) == 1 :
        return List
    elif len(List) > 1 :
        return recrev(List[(len(List)//2) : ]) + recrev(List[0:len(List)//2]) 
  
List2 = [1,2,3,4,6,7,9,14]    
print(recrev(List2))

#Task 4
def Fisher(A):
    for i in range(len(A)-2):
        j = rand.randint(i,len(A))
        A[j] , A[i] = A[j], A[i]
        return A

print(Fisher([1,2,3,4]))