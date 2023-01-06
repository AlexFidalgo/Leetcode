'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the 
integer. The digits are ordered from most significant to least significant in left-to-right order. The large 
integer does not contain any leading 0's.
'''

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
        
if __name__ == "__main__":
    print(plusOne([8,9,9]))
