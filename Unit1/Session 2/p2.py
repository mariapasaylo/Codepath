#U
#list of integers 
#print each item and multiple each number by 2 

#P
# Iterate through the list of integers
## Multiply current element by 2  
## then print current element 

#I
def doubled(lst):
    for i in lst:
        num = i * 2
        print(num)

#test
lst = [1,2,3]
doubled(lst)