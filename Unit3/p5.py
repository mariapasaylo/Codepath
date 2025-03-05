#U
#input string my_str
#output index of first non repeating character
#not exist return -1


#M dictionary, nested loop

#P
#Iterate through char in my_Str
#if current element is in currentIndex up until the end
    #move to next character
#else
    #currentElem is unique and save index
#return index

#I
def first_unique_char(my_str):
    #resultIndex = -1
    my_dict = {}
    for char in my_str:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict.update({char:1})
    index = 0
    for key, value in my_dict.items():
        if value == 1:
            return index
        index += 1

    return -1


#test
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
