def smallest_diff(x,y,z):
    assert type(x) == int and type(y) == int and type(z) == int
    diff1=abs(x-y)
    diff2=abs(x-z)
    diff3=abs(y-z)
    min_diff=min(diff1,diff2,diff3)
    return min_diff

smallest_diff(4,5,7)
print(smallest_diff(4,5,7))
