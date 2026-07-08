def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0 and a < b:
        return a
    elif a % 2 == 0 and b % 2 == 0 and a > b:
        return b
    elif a % 2 != 0 or b % 2 != 0 and a > b:
        return a
    elif a % 2 != 0 or b % 2 != 0 and a < b:
        return b
    

returned = lesser_of_two_evens(2,5)

print(returned)