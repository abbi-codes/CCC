def translate(c):
    c_ord = ord(c)
    if c_ord > ord('u'):
        vowel = 'u'
    else:
        if c_ord < ord('e'):
            front_vowel = 'a'
            back_vowel = 'e'
        elif c_ord < ord('i'):
            front_vowel = 'e'
            back_vowel = 'i'
        elif c_ord < ord('o'):
            front_vowel = 'i'
            back_vowel = 'o'
        elif c_ord < ord('u'):
            front_vowel = 'o'
            back_vowel = 'u'
        if (ord(back_vowel) - c_ord) >= (c_ord - ord(front_vowel)):
            vowel = front_vowel
        else:
            vowel = back_vowel

    for next_one in range(1, 3):
        if c == 'z':
            next_consonant = 'z'
        elif chr(c_ord + next_one) not in 'aeiou':
            next_consonant = chr(c_ord + next_one)
            break

    return (c + vowel + next_consonant)

word = input()
translated_word = ''
for letter in word:
    if letter in 'aeiou':
        translated_word += letter
    else:
        translated_word += translate(letter)
print(translated_word)