def sum_range(start_val,end_val):
    cnt = 0        #initialize accumulator to the default 0
    for x in range (start_val,end_val+1):
        cnt = cnt + x      #update: add new x value to the old value of cnt
    return cnt

print(sum_range(10,500))
