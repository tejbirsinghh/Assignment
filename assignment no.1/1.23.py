def starts_with(my_string, char):
    if my_string.startswith(char):
        return True
    else:
        return False

my_string = input("enter a string ")
my_char = input("enter a character ")

print("does the string '%s' starts with the character '%s'?" % (my_string, my_char))
print(starts_with(my_string, my_char))
