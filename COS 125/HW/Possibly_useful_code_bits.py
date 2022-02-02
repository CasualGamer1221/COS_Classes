

# # mylist=[[1,2,"hello"],[4,5],6]
# # mylist[0][2]=7
# # print(mylist)

# ##########################################################################################################
# list= [[0 for i in range(3)] for j in range(3)]
# print(list)
# 
# ##################  Print 2D LIST IN A GRID  #############################################################

# def boardprint():
#         for i in board:
#             print(' '.join(map(str, i)))
#         print()
# ######################################## 2 WAYS TO MAKE A 2D LIST #############
# result=[]
# for i in range(0,3):
#     temp=[]
#     for j in range(0,3):
#         temp.append(0)
#     result.append(temp)
# print(result)
        
# ############################  FACTORS OF NUMBER  ############################################################

# def factors(n):
#     factorsList=[]
#     for i in range(1,n+1):
#         if n%i == 0:
#             factorsList.append(i)
#     return factorsList
    

# factorslist=factors(n=int(input("What number do you want factors of? ")))
# print(factorslist)
# ############################################################################################################
