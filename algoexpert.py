# #Interview Prep


# # Question 1
# ################################################################################
# # Brute force method
# # 0(n^2) time. O(1) space

# def twoNumberSum1(array, targetSum):
#     for i in array:
#         for j in array:
#             if i == j:
#                 continue
#             if i + j == targetSum:
#                 return [i, j]

#     return []


# # If we value time complexity over space complexity
# # O(n) time. O(n) space
# def twoNumberSum2(array, targetSum):
#     myDict = {}
#     for num in array: 
#         if (targetSum - num) in myDict:
#             return [num, targetSum - num]
#         else:
#             myDict[num] = True
#     return []



# # If we value space complexity more than time complexity:

# # O(nlog(n)) time complexity
# # O(1) space complexity
# def twoNumberSum3(array, targetSum):
#     array.sort()

#     #left pointer and right pointer
#     left = 0
#     right = len(array) - 1
#     while left != right:
#         if array[left] + array[right] == targetSum:
#             return [array[left], array[right]]

#         elif array[left] + array[right] > targetSum:
#             right -= 1

#         else: # array[left] + array[right] < targetSum:
#             left += 1
#     return []

# ################################################################################


# # NOTE: O(n long(n)) > O(n)



# # Question 2
# ################################################################################



# # O(n) runtime 
# def isValidSubsequence(array, sequence):
#     if sequence.len() > array.len():
#         return False
    
#     for num in array: 
#         if sequence.len() == 0:
#             return True
#         elif num == sequence[0]:
#             sequence.pop(0)
        
#     return False

# ################################################################################


# .reverse has no return value

# Question 3
################################################################################
# O(n) time
# O(n) space
def sortedSquaredArray(array):
    # Write your code here.
    
    left = 0
    right = len(array) - 1
    
    sqArr = []
    
    while True:
        leftVal = array[left] ** 2
        rightVal = array[right] ** 2
        if left == right:
            sqArr.append(leftVal)
            break
        elif leftVal > rightVal:
            sqArr.append(leftVal)
            left += 1
        else:
            sqArr.append(rightVal)
            right -= 1

    sqArr.reverse()
    return sqArr
        
################################################################################
