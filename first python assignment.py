def split_balanced_string(s):
    balanced_strings = []
    count = 0
    curr_string = ""
    
    for char in s:
        curr_string += char
        if char == 'R':
            count += 1
        else:
            count -= 1
            
        if count == 0:
            balanced_strings.append(curr_string)
            curr_string = ""
    
    return len(balanced_strings), balanced_strings

# Read input string
s = input().strip()

# Split the balanced string
num_strings, strings = split_balanced_string(s)

# Print the number of balanced strings
print(num_strings)

# Print the balanced strings
for string in strings:
    print(string)
