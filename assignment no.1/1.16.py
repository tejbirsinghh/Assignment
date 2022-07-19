def insert_sting_middle(main_string, middle_string):
    main_len = len(main_string)
    middle = int(main_len/2)
    return main_string[:middle] + middle_string + main_string[middle:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))
