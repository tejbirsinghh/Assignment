from re import S


list = input('Please input a list of words to evaluate: ')
print(list)

longest = 0

for words in list.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words

print('The longest word is', longest_word, 'with length', len(longest_word))