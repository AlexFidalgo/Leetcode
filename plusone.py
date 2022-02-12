def plusOne(l):
    i = -1
    r = l.copy()
    c = 1
    while i >= (-len(l)):
        if c == 1:
            if l[i] == 9:
                r[i] = 0
            else:
                r[i] = r[i] + 1
                c = 0
        i = i - 1
    if c == 1:
        r = [1] + r
    return r
        
print(plusOne([9,9,9]))