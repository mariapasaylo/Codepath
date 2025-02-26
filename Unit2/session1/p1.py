

#Understand
#input list of integers lst and a list of integers sequence
#output true if subsequence and false if not

#lst [0, 2, 1, 9, -2, 3]
#sequence[1,3,-2]
#false

#Plan 
# create new list
# iterate through sequence
## iterate through lst
### if values in list are found in sequence, store them in a new list
# if new list has the same order as squence, then return true, else false


#Implement

def is_subsequence(lst, sequence):
    result = []
    #for num in sequence:
    for i in lst:
        if i in sequence:
            result.append(i)
    print(result)
    return result == sequence             
        
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print (is_subsequence(lst, sequence))





