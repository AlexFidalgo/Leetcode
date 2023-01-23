def countAndSay(n):  
    if str(n) == '1':
        return '1'
    s = countAndSay(n-1)
    return str(count_numbers(s))
    
def count_numbers(s):
    r = ''
    while s != '':
        d = s[0]
        c = 0
        while s[0] == d:
            c = c + 1
            s = s[1:]
            if s == '':
                break
        r = r + f'{c}{d}'
    return r
    
s = '50111'
print(count_numbers(s))
n = 11
print(countAndSay(n))

#%%
class Solution(object):
    def countAndSay(self, n):  
        if str(n) == '1':
            return '1'
        s = self.countAndSay(n-1)
        return str(self.count_numbers(s))
        
    def count_numbers(self, s):
        r = ''
        while s != '':
            d = s[0]
            c = 0
            while s[0] == d:
                c = c + 1
                s = s[1:]
                if s == '':
                    break
            r = r + "{}{}".format(c,d)
        return r
