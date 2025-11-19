def count_negatives(lst):
    if lst == []:
        return 0
    if lst[0] < 0:
        first = 1
    else:
        first = 0
    return first + count_negatives(lst[1:])

if __name__ == '__main__':
    print(count_negatives([4,5,-1,2,3,5,-7,-5,6]))
    print(count_negatives([0]))
