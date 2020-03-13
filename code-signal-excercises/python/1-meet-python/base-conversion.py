# Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

def baseConversion(n, x):
    return hex(int(n,x))[2:]

# Good to review bases and int() 
# also god using the slice syntac ( [:] )
# is so much easier than python