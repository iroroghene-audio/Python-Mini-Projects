def almost_there(n):
    if (n >= 90 and n <= 110) or (n >= 190 and n <= 210):
        return True
    else:
        return False
    


checker = almost_there(211)

print(checker)