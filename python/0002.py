# INSTRUCTIONS
# In this task, you need to write a Python function that finds repeating two-character patterns in a string. The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.

# Example:
# input = "aaababbababaca"
# ouput = "aa1ab2ba3ca1"

# Constraints
# The input string always has an even number of characters.
# The string contains only lowercase letters.
# The string length can be up to 500 characters.

def solution(input):
    output = ''
    pair_counter = 0
    pair = ''

    for i in range(0, len(input), 2):
        if i == 0:
            pair = input[i:i+ 2]
            pair_counter = 1
        else:
            if pair == input[i:i + 2]:
                pair_counter += 1
            else:
                output += pair
                output += str(pair_counter)
                pair = input[i:i + 2]
                pair_counter = 1

    output += pair
    output += str(pair_counter)

    return output
