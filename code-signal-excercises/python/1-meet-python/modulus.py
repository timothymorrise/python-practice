#Implement a function that, given a number n, returns -1 if this 
# number is not an integer and n % 2 otherwise. It is guaranteed 
# that if the number represents an integer, it will be written without 
# a decimal point.

def modulus(n):
    if isinstance(n, int):
        return n % 2
    else:
        return -1