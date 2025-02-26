#U
#list of integers 
#store each item and multiple each number by 2 in the new list
# return the new list

#P
# Create new list called result
# Iterate through the list of integers
## Multiply current element by 2 
## Add current element to result
#return result

#I
def doubled(lst):
    result = []
    for i in lst:
        num = i * 2
        result.append(num)
    return(result)

#test
lst = [1,2,3]
print(doubled(lst))