def change_start(value,lst):
    lst[0] = value
    return lst

t_list = ['a', 'b', 'c', 'd', 'e', 'f']
change_start('X', t_list)
print(t_list)
