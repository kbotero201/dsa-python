"""
In my experience, from most to least commonly mentioned in interviews:
1. quicksort: implement it, explain it
2. mergesort: implement it, talk about space complexity as well as time complexity
3. insertion sort: explain when it can be better than the above two
4. heapsort: explain how it works, and how heaps work in general
5. bubble sort: why it's awful
6. radix/counting/bucket sort: when it's useful
7. selection sort: usually thrown in as an example when asked to list sorting algorithms you know
"""

# Bubble Sort / Sinking Sort 
# O(n2) time complexity & O(1) space complexity 
def bubbleSort(list):
    for i in range(len(list) -1):
        for j in range(len(list) - i -1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)


# Selection Sort
# O(n2) time complexity & O(1) space complexity
def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    print(list)

# Insertion Sort 
# O(n2) time complexity & O(1) space complexity
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = key 
    print(list)

# Bucket Sort 
# O(n2) time complexity & O(n) space complexity
def bucketSort(list):
    numOfBuckets = round(math.sqrt(len(list)))
    maxValue = max(list)
    arr = []

    for i in range(numOfBuckets):
        arr.append([])
    for j in list:
        index_b = math.ceil(j* numOfBuckets/maxValue)
        arr.[index_b -1].append(j)
    
    for i in range(numOfBuckets):
        arr[i] - insertionSort(arr[i])
    
    k = 0
    for i in range(numOfBuckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k += 1
    return list 

# Merge Sort (divide and conquer algorithim)
# O(nlog n) time complexity & O(n) space complexity
def mergeSort(array):
    if len(array) <= 1:
        return array 
    midpoint = int(len(array)/2)

    left, right = mergeSort(array[:midpoint]), mergeSort(array[midpoint:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result 
 






