def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # the loop variable
    total = 0  # the accumulator variable
    while curr_val < topNum:
        total = total + curr_val  # add next value to accumulator
        curr_val = curr_val + 1  # update the loop variable

    return total

print(sum_to_n(10))