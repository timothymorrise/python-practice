a = True
b = False 
def func():
    print(a == (not b))
    print(not a == b)
    print(not (a == b))
func()
b = True
func()