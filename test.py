def animal_cracker(string):
    wordlist = string.lower().split()

    return wordlist[0][0] == wordlist[1][0]



print(animal_cracker('Llama dand'))

