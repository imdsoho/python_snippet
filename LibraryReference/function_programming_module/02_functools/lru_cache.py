from functools import lru_cache

@lru_cache(maxsize=128, typed=False)
def count_vowels(sentence):
    sentence = sentence.casefold()
    print("0", type(sentence), sentence)
    return sum(sentence.count(vowel) for vowel in 'aeiou')


sentence = "abc"
result = count_vowels(sentence)
print(count_vowels.__dict__)
print("1", count_vowels.cache_info())

print("------------------------")

# cache hits - count_vowels() 호출하지 않음
count_vowels(sentence)
print("2", count_vowels.cache_info())

print("------------------------")

# cache hits failed - count_vowels() 호출
other_str = "cache hit failed."
count_vowels(other_str)
print("3", count_vowels.cache_info())

#print(count_vowels.cache_clear())

