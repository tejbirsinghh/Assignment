def get_last_part(my_string, char):
    my_list = my_string.split(char)
    return char.join(my_list[:-1])

print(get_last_part('https://www.w3resource.com/python', "/"))
