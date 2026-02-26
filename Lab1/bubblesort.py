import time
import random

# Bubble sort
def bubbleSort(arr):
    swapped = False
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
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
            print(f"Time taken to sort {elements} elements using bubble sort is {tend - tstart:.4f} seconds")
        case 2:
            tstart = time.time()
            selectionSort(arr.copy())
            tend = time.time()
            print(f"Time taken to sort {elements} elements using selection sort is {tend - tstart:.4f} seconds")
        case 3:
            tstart = time.time()
            insertionSort(arr.copy())
            tend = time.time()
            print(f"Time taken to sort {elements} elements using insertion sort is {tend - tstart:.4f} seconds")









