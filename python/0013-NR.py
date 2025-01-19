"""
NOTES
    Took a lot of time to solve this and needed gpt help to understand the logic behind the solution
"""

def replace_substring(text, old, new):
    result = []

    pos = text.find(old)
    while pos != -1:
        result.append(text[:pos] + new)
        text = text[pos + len(old):]
        pos = text.find(old, pos + len(old))
    
    result.append(text)
    return ''.join(result)

print(replace_substring('this is a test', 'this', 'that'))
