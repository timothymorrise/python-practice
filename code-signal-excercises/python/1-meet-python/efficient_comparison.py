import timeit
def integer_in_bounds_1(x, y, L, R):
    if L < x ** y <= R:
        return True
    return False

def integer_in_bounds_2(x, y, L, R):
    if x ** y > L and x ** y <= R:
        return True
    return False

def integer_in_bounds_3(x, y, L, R):
    if x ** y in range (L + 1, R + 1):
        return True
    return False

x = 3
y = 2
L = 7
R = 10

print(timeit.timeit('integer_in_bounds_1(x, y, L, R)', 'from __main__ import integer_in_bounds_1, x, y, L, R'))
print(timeit.timeit('integer_in_bounds_2(x, y, L, R)', 'from __main__ import integer_in_bounds_2, x, y, L, R'))
print(timeit.timeit('integer_in_bounds_3(x, y, L, R)', 'from __main__ import integer_in_bounds_3, x, y, L, R'))

# NOTES:
# remember your types: and that timeit only passes strings
