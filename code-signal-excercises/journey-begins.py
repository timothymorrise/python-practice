def add(param1, param2):
    return param1 + param2

def centuryFromYear(year):
    return math.ceil(year/100)

def checkPalindrome(str):
    def checkPalindrome(string):
    length = len(string)
    print(length)
    for i, v in enumerate(string): 
        current_character = v
        reverse_length = length - i - 1
        reverse_character = string[reverse_length]
        if v != reverse_character:
            return False 
    return True

