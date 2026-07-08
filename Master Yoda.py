def master_yoda(string):
    modified_string = []
    index = len(list(string))
    
    return ' '.join(string.split()[::-1])
    

print(master_yoda('How are you'))