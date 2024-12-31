"""
INSTRUCTIONS
You are given a string filled with words. Your task is to write a Python function that takes this string as input. Your function should then capitalize the first letter of each word while making the rest of the letters lowercase. Finally, it should recombine the words into a new string where every word starts with a capital letter.

CONSTRAINTS
The input string will contain between 1 and 100 words.
Each word is a sequence of characters separated by white space.
Words consist of characters ranging from a to z, A to Z, 0 to 9, or even an underscore _.
The provided string will not start or end with a space, and it will not contain double spaces.
After capitalizing the first character of each word and converting the rest to lowercase, the program should return a single string in which the words maintain their original order.
If the first character of a word is not a letter (like a number or an underscore), keep it as is.

EXAMPLE
input: 'SoME rAndoM _TeXT'
output: 'Some Random _text'


====================================================================================================


THOUGH PROCCESS
    1. Split all words in a list
    2. Transform every word in the list to lower case
    3. Analyze the first letter of each word
        3.1 First letter are in a-z range
            Change first letter to Upper case
        3.2 First letter are NOT in a-z range
            Do nothing
    4. Add the word to a output list
    5. Return the output join all the words in the list
"""

def solution(input_str):
    words = input_str.split()
    output = []

    for w in words:
        w = w.lower()
        if w[0].isalpha():
            w = w[0].upper() + w[1:]

        output.append(w)

    return ' '.join(output)


print(solution("SoME rAndoM _TeXT"))
