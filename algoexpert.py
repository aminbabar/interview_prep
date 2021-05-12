#Interview Prep


# Question 1
################################################################################
# Brute force method
# 0(n^2) time. O(1) space

def twoNumberSum1(array, targetSum):
    for i in array:
        for j in array:
            if i == j:
                continue
            if i + j == targetSum:
                return [i, j]

    return []


# Smart method
# O(n) time. O(n) space
def twoNumberSum2(array, targetSum):
    myDict = {}
    for num in array: 
        if (targetSum - num) in myDict:
            return [num, targetSum - num]
        else:
            myDict[num] = True
    return []



# Smartest method
# O(nlog(n)) time complexity
# O(1) space complexity
def twoNumberSum3(array, targetSum):
    array.sort()

    #left pointer and right pointer
    left = 0
    right = len(array) - 1
    while left != right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]

        elif array[left] + array[right] > targetSum:
            right -= 1

        else: # array[left] + array[right] < targetSum:
            left += 1
    return []

################################################################################



# Question 2
################################################################################








