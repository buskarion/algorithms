"""
INTRUCTIONS
Let's imagine you are given a string that contains a series of words separated by a hyphen ("-"). Each word in the string can be a lowercase letter from 'a' to 'z' or a set of digits representing a number from 1 to 26. Your task is to parse this string and swap the type of each word: convert numbers into their corresponding English alphabet letters, and letters into their numerical equivalents. This means '1' should convert to 'a', and 'a' should convert to '1'.
You need to return a new string with the converted words, rejoined with hyphens.
Ensure you maintain the original order of the words from the input string in your output string.

CONSTRAINTS
The input string's length should range from 1 to 1000 for this exercise. The string will never be empty, always containing at least one valid lowercase letter or numerical word.
Remember, the transformation of words should be limited to converting numbers from 1 to 26 into their corresponding letters from 'a' to 'z', and vice versa.

EXAMPLE
input: '1-a-3-c-5'
input: 'a-1-c-3-e'

========================================================================================================

THOUGHT PROCESS
    1. Split the words in the string into a list
    2. Iterate over the list
    3. Verify if it is a letter:
        3.1 It is a letter:
            Get the int value of the letter
            To do that, we can use the ASCII values with formula: ASCII(z) - ASCII(a) + 1
        3.2 It is not a letter:
            So, it's a number. Get the letter that number represents.
            To do that, we can use the ASCII values with the formula: ASCII(a) + number - 1
    4. Append the value to an output list in a string format
    5. Return the output

NOTES
    A. During the implementation, I notice that the formula to get the number value, is wrong. The correct way to think is:
        1. If we do ASCII(z) - ASCII(a) we get 25
        2. The value that represents the letter 'a' is 1. So, if we subtract the CONSTANT value ASCII(z) - ASCII(a) from 26, we get the correct value for 'a' which is 1.
    B. I am noticing that on of the keys to solve problems is to found the constant values. I will keep it in mind for the next exercises.
    
"""

def solution(s):
    words = s.split('-')
    output = []

    for w in words:
        if w.isalpha():
            output.append(str(26 - (ord('z') - ord(w))))
        else:
            output.append(chr(ord('a') + int(w) - 1))

    return '-'.join(output)

print(solution("1-a-3-c-5"))
