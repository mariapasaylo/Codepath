#
#integer list nums
#return list with front part even and rest is odd

#M 2 pointer

#P
'''
INitlize a left pointer
initlizea right pointer 
iterate through it 
we check if left is odd, and if right is odd then we move left eighter infront of right or behind
we check if left is odd and right is even then we move the right to the left eighter infront or behind
we check if both are even then we move the the right to the left 

'''
#I
def sort_array_by_parity(nums):

    left, right = 0, len(nums) - 1
    while(left<right):
        

    pass

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))