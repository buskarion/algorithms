# INTRUCTIONS
# You are given a string of n characters, with n varying from 1 to 1000, inclusive. Your task is to write a Python function that takes this string as input, applies the following operations, and finally returns the resulting string.

# CONSTRAINTS
# The input string will neither start nor end with a space, nor will it have multiple consecutive spaces.
# Each word will contain only alphabets and digits, and its length will range from 1 to 10.
# The words are case-sensitive; for example, 'word' and 'Word' are considered distinct.

# EXAMPLE
# input = "abc 123 def"
# output = "cab 312 fde"

def solution(input):
    words = input.split()
    words_characters_shifted_by_1 = []

    for w in words:
        shifted_word = w[-1] + w[:len(w) - 1]
        words_characters_shifted_by_1.append(shifted_word)

    return ' '.join(words_characters_shifted_by_1)

print(solution("abc 123 def"))
