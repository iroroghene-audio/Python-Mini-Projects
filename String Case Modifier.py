def string_modifier(string):
    modified_string = []
    index = 0

    for char in list(string):
        if index % 2 == 0:
            modified_string.append(char.upper())
        else:
            modified_string.append(char.lower())
        index += 1

    return ''.join(modified_string)



new_string = string_modifier('Xylophone')

print(new_string)

