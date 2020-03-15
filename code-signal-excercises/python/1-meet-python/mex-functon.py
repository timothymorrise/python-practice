# For the given set s and given an upperBound, implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.

def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound
    return found