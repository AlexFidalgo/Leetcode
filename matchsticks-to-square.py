############## My solution (exceeds time limit) #####################

def makesquare(matchsticks):
    q = [0, 0, 0, 0]

    for comb in product([0,1,2,3], repeat=len(matchsticks)):
        for i, v in enumerate(comb):
            q[v] = q[v] + matchsticks[i]
        
        if q[0] == q[1] == q[2] == q[3]:
            return True
        
        q = [0, 0, 0, 0]

    return False

def product(*args, repeat=1):

    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

print(makesquare([3,3,3,3,4]))
print(makesquare([1,1,2,2,2]))

############## Correct solution #####################
# https://leetcode.com/problems/matchsticks-to-square/solutions/1273708/python-dp-on-subsets-explained/?orderBy=most_votes

from functools import lru_cache

def makesquare2(nums):
    N = len(nums)
    basket, rem = divmod(sum(nums), 4)
    if rem or max(nums) > basket: return False
    
    @lru_cache(None)
    def dfs(mask):
        if mask == 0: return 0
        for j in range(N):
            if mask & 1<<j:
                neib = dfs(mask ^ 1<<j)
                if neib >= 0 and neib + nums[j] <= basket:
                    return (neib + nums[j]) % basket
        return -1
                
    return dfs((1<<N) - 1) == 0

print(makesquare2([3,3,3,3,4]))
print(makesquare2([1,1,2,2,2]))

############## Another correct solution #####################
# https://leetcode.com/problems/matchsticks-to-square/solutions/95732/python-dfs-solution/?orderBy=most_votes

def makesquare3(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def dfs(nums, pos, target):
        if pos == len(nums): return True
        for i in range(4):
            if target[i] >= nums[pos]:
                target[i] -= nums[pos]
                if dfs(nums, pos+1, target): return True
                target[i] += nums[pos]
        return False
    if len(nums) < 4 : return False
    numSum = sum(nums)
    nums.sort(reverse=True)
    if numSum % 4 != 0: return False
    target = [numSum/4] * 4;
    return dfs(nums,0, target)

print(makesquare2([3,3,3,3,4]))
print(makesquare2([1,1,2,2,2]))
