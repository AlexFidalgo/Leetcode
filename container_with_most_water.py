"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line 
are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

https://leetcode.com/problems/container-with-most-water/description/
"""

def maxAreaBruteForce(height):
    # Yields 'Time Limit Exceeded'
    
    max_vol = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            if height[i] > height[j]:    
                vol = (j-i)*height[j] 
            else:
                vol = (j-i)* height[i]
            if vol > max_vol:
                max_vol = vol
    return max_vol

def maxArea(height):
    left = 0
    right = len(height) - 1
    res = 0

    while right > left:
        a = (right-left)*min(height[right], height[left])
        res = a if a > res else res

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return res
        

print("--teste 1")
height = [1,8,6,2,5,4,8,3,7]
print("maxAreaBruteForce: ", maxAreaBruteForce(height))
print("maxArea: ", maxArea(height))
print()
print("--teste 2")
height = [1,1]
print("maxAreaBruteForce: ", maxAreaBruteForce(height))
print("maxArea: ", maxArea(height))
