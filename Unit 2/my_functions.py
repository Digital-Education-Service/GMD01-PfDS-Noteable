def isItChristmas(month, day):
    return month == 12 and day == 25

isItChristmas(day=25, month=12)

def countLetters(inputString, letter = 'a'):
    inputString = inputString.lower()
    total = 0
    for l in inputString:
        if l == letter:
            total += 1
    return total

def long_words_after_l(words):
    keep_words=[]
    for word in words:
        if word[0]>'l' and len(word)>6:
            keep_words.append(word)            
    return keep_words