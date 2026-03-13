import time
import random

# Bubble sort
def bubbleSort(arr):
    swapped = False
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

# Selection Sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range (i+1 , n):
            if arr[j] < arr[min_idx]:
              min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion sort
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1
        arr[j + 1] = key

# Merge Sort
def merge(arr, left, right):
    middle = (right + left) // 2
    nL = middle - left + 1
    nR = right - middle

    L = [0] * nL
    R = [0] * nR

    for i in range(nL):
        L[i] = arr[left + i]
    for j in range(nR):
        R[j] = arr[middle + 1 + j]

    i = 0 # Index for left Array
    j = 0 # ,,    ,,  right ,, 
    k = left 

    while i < nL and j < nR:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < nL:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < nR:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSortT(arr, left, right, threshold):
    currentSize = right - left + 1
    
    if currentSize <= threshold:
        subArray = arr[left : right + 1]
        selectionSort(subArray)
        arr[left : right + 1] = subArray
        return 
    
    if left < right:
        mid = (right + left) // 2
        mergeSortT(arr, left, mid, threshold)
        mergeSortT(arr, mid + 1, right, threshold)
        merge(arr, left, right)

def mergeSort(arr, left, right):
    if left < right:
        mid = (right + left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, right)

# Quick Sort
# TODO
 
# Heap Sort
# TODO        
    
elements = int(input("Enter number of elements: "))

while elements < 10000:
    elements = int(input("Value must be >= 10000\nEnter number of elements: "))
arr = [random.randint(1, 999999) for _ in range(elements)]

while True:
    choice = int(input("1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\nCtrl + C to exit\nEnter the sorting algorithm you want: "))
    while choice < 1 or choice > 3:
        choice = int(input("Your choice must be either 1, 2 or 3\nEnter your choice: "))
    match choice:
        case 1:
            tstart = time.time()
            bubbleSort(arr.copy())
            tend = time.time()
            print(f"Time taken to sort {elements} elements using bubble sort is {1000*(tend - tstart):.4f} ms")
        case 2:
            tstart = time.time()
            selectionSort(arr.copy())
            tend = time.time()
            print(f"Time taken to sort {elements} elements using selection sort is {1000*(tend - tstart):.4f} ms")
        case 3:
            tstart = time.time()
            insertionSort(arr.copy())
            tend = time.time()
            print(f"Time taken to sort {elements} elements using insertion sort is {1000*(tend - tstart):.4f} ms")