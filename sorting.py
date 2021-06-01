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
