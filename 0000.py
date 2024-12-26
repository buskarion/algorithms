# TASK
# Writh a function that implements the concept of Run-Length Encoding (RLE) on an alphanumerical input string

# INPUT: string
# OUTPUT: string

# CONTRAINTS
# should operate only on alphanumeric characters
# input string length should have up to 500 characters

# EXAMPLES:
# CASE 1:
# input: "aaabbcccdde"
# output: "a3b2c3d2e1"

# CASE 2:
# input: "aaa@@bb!!c#d**e"
# input: "a3b2c1d1e1"

def encode_rle(input):
    current_char = None
    current_char_count = 0
    output = ""
    
    for c in input:
        if c.isdigit() or c.isalpha():
            if current_char is None:
                current_char = c
                current_char_count = 1
            else:
                if current_char == c:
                    current_char_count += 1
                else:
                    output += current_char
                    output += str(current_char_count)
                    current_char = c
                    current_char_count = 1

    if current_char is not None:
        output += current_char
        output += str(current_char_count)

    return output

print(encode_rle("aaa@@bb!!c#d**e"))
