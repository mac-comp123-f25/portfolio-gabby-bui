def square_user_nums():
  # Initialize loop variable
  user_inp = input("Enter the next number (negative to quit): ")
  user_num = int(user_inp)
  while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")

square_user_nums()