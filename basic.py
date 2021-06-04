#myList = [1,2,3,4,5,6,7,10]

# Find missing number in an integer array of 1 to 100
# Formula: n(n+1)/2
# def findMissing(list, n):
#     sum1 = 100(101)/2
#     sum2 = sum(list)
#     print(sum1-sum2)


# Write a program to find all pais of integers whose sum is equal to a given number
# [2,6,3,9,11] target: 9 => [6,3]
# Does array contain only positive or negative numbers?
# What if the same pair repeats twice, should I print every time?
# If the reverse of the reverse of the pair is acceptable, can we print both (4,1) and (1,4) if the given sum is 5
# Do we need to print only distinct pairs? does (3,3) count as a valid pair for given sum 6?
# How big is the array?

# Must be distinct (2,2) or (3,3) not a valid pair 
def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]: # for distinct pairs 
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

myList = [1,2,3,2,3,4,5,6]
#findPairs(myList, 6)




# def twoSum1(self, nums, target):
# 		buffer_dictionary = {}
# 		for i in rangenums.__len()):
# 			if nums[i] in buffer_dictionary:
# 				return [buffer_dictionary[nums[i]], i] #if a number shows up in the dictionary already that means the 
# 														#necesarry pair has been iterated on previously
# 			else: # else is entirely optional
# 				buffer_dictionary[target - nums[i]] = i 
# 				# we insert the required number to pair with should it exist later in the list of numbers

def twoSum2(self, nums, target):
        buffer = {}
        for i, num in enumerate(nums):
            m = target - num
            if m in buffer:
                return [buffer[m], i]
            else:
                buffer[num] = i


# O(n) time complexity & O(n) space complexity
def twoSum3(nums, target):
    dic = {}
    result = []
    for i, num in enumerate(nums): 
        if num in dic:
            result.append([dic[num], i])
        dic[target-num] = i
    print(dic)
    return print(result)

twoSum3(myList, 6)


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# O(n) time complexity & O(1) space complexity 
# all lowercase letters and no unicode characters
def isAnagram2(s, t):
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True

