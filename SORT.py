import time

import random

# Generate a large unsorted array with 100,000 random integers
large_array = [random.randint(1, 1000000) for _ in range(1000000)]




def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def selection_sort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
        if i != min:
            list[i], list[min] = list[min], list[i]
    return list

def insertion_sort(list):
    for i in range(1,len(list)):
        value = list[i]
        j = i-1
        while list[i] < list[j] and j >= 0:
            list[j+1] = list[j]
            list[j] = value
            j-=1
    return list

def merge(list1,list2):
    i = 0
    j = 0
    combine = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combine.append(list1[i])
            i+=1
        else:
            combine.append(list2[j])
            j+=1
    while i < len(list1):
        combine.append(list1[i])
        i+=1
    while j < len(list2):
        combine.append(list2[j])
        j+=1
    return combine

def merge_sort(list):
    if len(list) == 1:
        return list
    midPoint = int(len(list) / 2)
    left = merge_sort(list[:midPoint])
    right = merge_sort(list[midPoint:])
    return merge(left,right)

def swap(my_list,index1,index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
def pivot(my_list,pivot_ind, end_ind):
    swap_ind = pivot_ind
    for i in range(pivot_ind+1, end_ind+1):
        if my_list[i] < my_list[pivot_ind]:
            swap_ind +=1
            swap(my_list,swap_ind,i)
    swap(my_list,pivot_ind,swap_ind)
    return swap_ind

def quick_sort_helper(my_list,left,right):
    if left < right:
        pivot_ind = pivot(my_list,left,right)
        quick_sort_helper(my_list,left,pivot_ind-1)
        quick_sort_helper(my_list,pivot_ind+1,right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list,0,len(my_list)-1)
        
        


my_list = [4,2,6,5,1,3]

# print(large_array)



#BUBBLE

# timeB1 = time.time()
# bubble_sort(large_array)
# timeB2 = time.time()  
# processB = (timeB2 - timeB1) * 1000
# print(f"processing time using Bubble Sort is",processB, "ms")


# #SELECTION

# timeS1 = time.time()
# selection_sort(large_array) 
# timeS2 = time.time()  
# processS = (timeS2 - timeS1) * 1000 
# print(f"processing time using Selection Sort is",processS, "ms")


#SORTED FUNCTION

time1 = time.time()
sorted(large_array)
time2 = time.time()
process = (time2 - time1) * 1000
print(f"processing time using Sorted Function is",process, "ms")



#INSERTION

timeI1 = time.time()
insertion_sort(large_array) 
timeI2 = time.time() 
processI = (timeI2 - timeI1) * 1000 
print(f"processing time using Insertion Sort is",processI, "ms")


#MERGE

timeM1 = time.time()
sorted = merge_sort(large_array)
timeM2 = time.time()   
processM = (timeM2 - timeM1) * 1000
print(f"processing time using Merge Sort is",processM, "ms")



#QUICK

timeQ1 = time.time()
quick_sort(large_array)
timeQ2 = time.time()
processQ = (timeQ2 - timeQ1) * 1000
print(f"processing time using Quick Sort is",processQ, "ms")

# print(len(sorted))
# print(sorted)




    