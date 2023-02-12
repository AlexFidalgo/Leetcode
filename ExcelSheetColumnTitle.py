#https://leetcode.com/problems/excel-sheet-column-title/description/
def convertToTitle(c):
    
    al =[chr(i) for i in range(ord('A'),ord('Z')+1)]
    
    res = ''
    while c > 0:    
        ch = c - int(c/26)*26
        res = al[ch-1]+ res
        c = int((c-1)/26)
    
    return res
