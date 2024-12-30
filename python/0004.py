# INTRUCTIONS
    # Given a string consisting of words separated by whitespace, your task is to write a Python function that accepts this string. It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches them all together to form a new string.

# CONSTRAINTS
    # The input string will include between 1 and 100 words.
    # Each word consists of characters separated by white space.
    # A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
    # The given string will not start or end with a space, and there will be no occurrence of double spaces.
    # After transforming the characters of the words, form a new string by taking the last word first and appending the remaining words in their original order, each separated by spaces.

# EXAMPLE
    # input: "CapitaL letters"
    # output: "ovggvih XzkrgzO"

"""
    THOUGHT PROCCESS
        1. Get the ASCII value of the current character
        2. Identify from which edge the current character are closer, e.g, the beggining (a-A) or the end (z-Z)
        3. Identify for how much the current value are away from its nearest edge
        4. Now, there are two possible cases:
            4.1 The current character are closer from 'a-A', for instance, the current character value is 'c'
                In this case, 'c' has the value 99, it means that its distance is ASCII(c) - ASCII(a) which is equals to 2
                So, its opposite should be 2 values away from 'z', which means ASCII(z) - 2 or ASCII(z) - (ASCII(c) - ASCII(a))
            4.2 The current character are closer from 'z-Z'
                Here is the same logic, except that we will add the "distanca value" instead of subtract
                Let's use the character 'x' for example. It's disntance from the nearest edge is ASCII(z) - ASCII(x) = 2
                So, its opposite is ASCII(z) - ASCII(x) + ASCII(a)
            
            LOGIC CONCLUSION
                Doing the though proccess on item 4, we just have concluded that the equation to find its opposite independent of where it is, is the same, which is ASCII(z) - ASCII(char_you_want_to_find) + ASCII(a)
                So, it does't metter of which side it its, we can use the same equation avoiding to use a conditional

    NOTES:
        1. After the implementation of the logic above, I notice that I misunderstood the problem. I didn't notice the requirement of putting the last word first, so a I did waste a lot of time on it because a lack of attention
        2. Also, I did have some trouble to implement the logic about the logic above. It got me some time.
"""

def solution(input):
    words = input.split()
    opposite_words_list = []
    opposite_word = ""

    for w in words:
        for c in w:
            if ord(c) <= ord('Z'):
                opposite_word += chr(ord('Z') - ord(c) + ord('A'))
            else:
                opposite_word += chr(ord('z') - ord(c) + ord('a'))

        opposite_words_list.append(opposite_word)
        opposite_word = ""

    response = [opposite_words_list[-1]]
    opposite_words_list.pop()
    response.extend(opposite_words_list)
    return ' '.join(response)

print(solution("CapitaL letters"))
                
        
