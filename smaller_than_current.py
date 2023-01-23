def smallerNumbersThanCurrent(nums):
    """
    Time: O(n²)
    Space: O(1)
    """
    res = []
    for i_cur, cur in enumerate(nums):
        count = 0
        for i_x, x in enumerate(nums):
            if i_cur != i_x and cur > x:
                count = count + 1
        res.append(count)
    return res
  
def smallerNumbersThanCurrentOptimal(nums):
  """
  We sort the list (we don't want to keep traversing the list back and forth) and store in another temp list. 
  We traverse temp list. If we find unique element, we know all the previous elements have been recorded. 
  So we add this unique element to the dictionary with index i as value.
  If duplicate element is encountered, we don't add it and don't update the value in dictionary.
  After the dictionary is constructed, we create output after doing O(1) lookup in dictionary for nums[i].
  
  Time: O(n*log(n)) #sorting
  Space: O(n) #dictionary
  """
  temp = sorted(nums)
  mapping = {}
  result = []
  for i in range(len(temp)):
      if temp[i] not in mapping:
          mapping[temp[i]] = i
  for i in range(len(nums)):
      result.append(mapping[nums[i]])
  return result
  
print(smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
print(smallerNumbersThanCurrentOptimal(nums = [8,1,2,2,3]))
