#U
# function: two dict parameter and get the common key value
# return common list

#M

#P
#Create a list to store result 
#Take the the keys from first and second dictionary
#iterate through first list
##iterated through second list
###compare if item in first list is in second list
## store in result

#OR
#use the set intersection of the dictionaries
####
#return result

#I
def common_keys(dict1, dict2):
    result = []
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    return list(keys1 & keys2)
    
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
