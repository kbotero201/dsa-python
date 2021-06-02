#myList = [1,2,3,4,5,6,7,10]

# Find missing number in an integer array of 1 to 100
# Formula: n(n+1)/2
def findMissing(list, n):
    sum1 = 100(101)/2
    sum2 = sum(list)
    print(sum1-sum2)


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
                print(i,j)

myList = [1,2,3,2,3,4,5,6]
findPairs(myList, 6)