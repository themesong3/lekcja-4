def checkLetter(letter, word):
    l_counter = 0
    for i in range(len(word)):
        if letter == word[i]:
            l_counter += 1
    return l_counter

print(checkLetter("e", "You never get a second chance to make a first impression"))
    