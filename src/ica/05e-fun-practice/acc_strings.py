def copy_str(string,num_times):
    ans_str = ""     #initialize accumulator to empty string
    for x in range (num_times):
        ans_str = ans_str + " " + string
    return ans_str

print(copy_str("minehahaha",10))