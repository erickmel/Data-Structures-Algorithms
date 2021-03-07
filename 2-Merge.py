# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:05:05 2020

@author: Erick
"""

# Data Structures - 2 merge Sorted arrays

def mergeSortedArrays(arr1, arr2):
    i = 0
    j = 0
    mergedArray = []
    while(i < len(arr1) and j < len(arr2)):
        print(i, j)

        if(arr1[i] < arr2[j]):
            mergedArray.append(arr1[i])
            i += 1
    
        elif(arr1[i] >= arr2[j]):
            mergedArray.append(arr2[j])
            j += 1

    return mergedArray

a = [1, 2, 5, 8, 12, 15]
b = [3, 5, 6,  7, 9, 13, 13, 17, 20]

c = mergeSortedArrays(a, b)
print(c)
