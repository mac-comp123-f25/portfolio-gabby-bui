def string_of_nums(n):
    result = ""
    for i in range (1,n+1):
        result = result + " " + str(i)
    return result

print(string_of_nums(10))
