
print("[1]", locals())

def count_vowels(sentence):
    sentence = sentence.casefold()
    print(type(sum))
    return sum(sentence.count(vowel) for vowel in 'aeiou')

print("[2]", locals())

sum = 10
sentence = "abc"

print("[3]", locals())

count_vowels(sentence)  # ERROR

'''
[1] {'__name__': '__main__', ... '__cached__': None}
[2] {'__name__': '__main__', ... '__cached__': None, 'count_vowels': <function count_vowels at 0x002033>}
[3] {'__name__': '__main__', ... '__cached__': None, 'count_vowels': <function count_vowels at 0x002033>, 'sum': 10, 'sentence': 'abc'}
'''
