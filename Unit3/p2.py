#U 
# swap the first and last characters of the input parameter, my_str
# returns the new string 

# P 
# first letter = my_str[0]
# last letter = my_str[-1]  # minus smtg?? 1 
# middle_Letters = my_str[1:-2]
# retrun concatenated (last + middle_Letters + first)

# I 

def swap_ends(my_str):
    first = my_str[0]
    last = my_str[-1]
    middle = my_str[1:-1]
    return last+middle+first

#test
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)