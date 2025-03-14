#U
#1 and itself== prime number 
#Integer 
#M
#modulo

#P
'''
we check if its not prime
Iterate through the loop 
check if its prime(module remainder is zero)
'''
#I
def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


#test

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))


