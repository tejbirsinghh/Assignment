text = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in text.split()]

# sort the list
words.sort()

# display the sorted words
print("The sorted words are:")
for word in words:
   print(word)