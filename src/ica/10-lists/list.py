test_list  = [1, 2, 3, 4, 5, 6]
test_list[3] = 105
test_list[0] = 99
test_list[4:6] = [25, 26]
test_list[1:3] = [-5]

del test_list[1]
del test_list[3:5]

print(test_list)