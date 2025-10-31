def every_other(lst):
    return print(lst[::2])

every_other(['a', 'b', 'c'])

def sum_positive(lst):
    sum = 0
    for x in lst:
        if x > 0:
            sum += x
    return print(sum)

sum_positive([1,2,3,4,5,-5])
