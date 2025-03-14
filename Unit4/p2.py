#U
#list of elements
#return the list in reverse
#inplace - no new list

#M two pointer problem

#P
#initialize left 0, right length of list -1
#while the left is less than the right
## store left in temporary variable
## store right right in temporary variable
## update list at position right to temp left
## update list at position left to temp right
## increment left and decrement right
#return lst

#I
def reverse_list(lst):
    #initialize left 0, right length of list -1
    left = 0
    right = len(lst) - 1
    #while the left is less than the right
    while (left < right):
        temp_left = lst[left]
        temp_right = lst[right]
        lst[left] = temp_right
        lst[right] = temp_left
        left+=1
        right-=1
    return lst

#T

print(reverse_list([1,2,3,4,5]))