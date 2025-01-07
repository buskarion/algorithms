"""
THOUGHT PROCESS
    1. Split the input string into a list of words
    2. Strip non alphanumerical characters from words that contain digits
    3. Store the digit on an auxiliary variable
    4. Add the digit to the next word at position 1
    5. Append the word at a final list
    6. Return the output

NOTES DURING THE IMPLEMENTATION
    1. I had some problem with words that contains not alphanumerical characters like 'Let's'
    2. Other problem with the steps above is that the digit remain on its position instead of being removed after beeing added to the next word

SOLUTION
    Validate the word by being a digit, not alpha. If it not a digit, its added to output list. This way, we fix the 2 issues above
        
"""

def solution(input_str):
    words = input_str.split()
    aux = ''
    output = []
    
    for w in words:
        if aux != '':
            output.append(w[0] + aux + w[1:])
            aux = ''
        elif not w.isdigit():
            output.append(w)

        for c in w:
            if c.isdigit():
                aux += c

    return ' '.join(output)


print(solution("Let's meet at 7 at the clock tower."))
