str1 = input('Please Enter First String : ')
str2 = input('Please Enter Second String : ')

x = str2[:2] + str1[2:]
y = str1[:2] + str2[2:]

print('Your first has become :- ',x)
print('Your second has become :- ',y)
print('Your combined string is:-',x + ' ' + y)