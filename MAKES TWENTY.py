def makes_twenty(a, b):
    if a + b == 20 or a == 20 or b == 20:
        return True
    else:
        return False
    

checker = makes_twenty(2, 3)

print(checker)