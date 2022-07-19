string=input('Enter the string:')
n=int(input('Enter the index of the character to remove:'))
first = string[:n]   
last = string[n+1:]  
print('Modified string:',first+last)
