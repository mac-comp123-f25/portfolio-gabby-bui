def add_user_nums():
    sum_of_nums = 0
    user_num = int(input("Enter a number (enter zero to quit): "))
    while user_num > 0:
        sum_of_nums = sum_of_nums + user_num
        user_num = int(input("Enter a number (enter zero to quit): "))

    return print("The sum of the numbers entered is: ", sum_of_nums)

add_user_nums()