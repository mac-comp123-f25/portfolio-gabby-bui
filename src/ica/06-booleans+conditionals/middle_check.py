def middle_value(a,b,c):
    if a < b:
        if b < c:
            return b
        else:
            return c

    elif b < c:
        if c < a:
            return c
        else:
            return a

    else:
        if a < c:
            return a
        else:
            return c

print(middle_value(7,3,4))