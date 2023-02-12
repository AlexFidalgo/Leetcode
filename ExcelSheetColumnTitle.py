#https://leetcode.com/problems/excel-sheet-column-title/description/

#It is like in a number system in which after 9 it is 00 instead of 10; or like a system without zero: starting with 1, 2.. and after 9 it is 11.
def convertToTitle(c):
    
    al =[chr(i) for i in range(ord('A'),ord('Z')+1)]
    
    res = ''
    while c > 0:    
        ch = c - int(c/26)*26
        res = al[ch-1]+ res
        c = int((c-1)/26)
    
    return res
