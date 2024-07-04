input_string = "$180,240/y"

# Removing the special  characters using iteration on each character in string and joining back the characters in one string 

num_string = ''.join(filter(str.isdigit, input_string))

# Convert the num string variable to an integer using  int 
output_integer = int(num_string)

print(f"Input String =", input_string)
print(f"Output Integer =", output_integer)
