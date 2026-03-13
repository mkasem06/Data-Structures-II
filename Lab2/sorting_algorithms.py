import time
import random

#Quick Sort Algorithm
#partiton function
def partition(arr, low, high):
    randomIndex = random.randint(low, high)
    arr[high], arr[randomIndex] = arr[randomIndex], arr[high]
    pivot = arr[high]
    i = low
    for j in range (low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

#Quick Sort
def quickSort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        quickSort(arr, low, index - 1)
        quickSort(arr, index + 1, high)

#kth smallest element (task 8)
def kthSmallest(arr, low, high, k):
    if low <= high:
        index = partition(arr, low, high)
        if index == k - 1:
            return arr[index]
        elif k - 1 < index:
            return kthSmallest(arr, low, index - 1, k)
        else:
            return kthSmallest(arr, index + 1, high, k)

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


# Heap Sort
def heapify(arr,i,n):
    largest = i
    L = 2*i
    R =2*i +1
    if L <= n and arr [largest] < arr[L]:
        largest = L
    if R <= n and arr[largest] < arr[R]:
        largest = R

    if largest !=i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)

def buildHeap(arr):
    n = len(arr) -1
    for i in range(n//2  , 0, -1):
        heapify(arr, i, n)

def heapSort(arr):
    n = len(arr) -1
    buildHeap(arr)
    for i in range(n , 1, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heapify(arr, 1, i-1)


def to_heap_array(lst):
    return [None] + list(lst)
 
def from_heap_array(A):
    return A[1:]



elements = int(input("Enter number of elements: "))

while elements < 10000:
    elements = int(input("Value must be >= 10000\nEnter number of elements: "))
arr = [random.randint(1, 999999) for _ in range(elements)]

while True:
    choice = int(input("1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Quick Sort\n5. Merge Sort\n6. Heap Sort\n7. Hybrid Merge Sort\n8. Find Kth smallest element\n9. Exit\nEnter your choice: "))
    while choice < 1 or choice > 9:
        choice = int(input("Your choice must between 1 and 6\nEnter your choice: "))
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
        case 4:
            tstart = time.time()
            quickSort(arr.copy(), 0, len(arr) - 1)
            tend = time.time()
            print(f"Time taken to sort {elements} elements using quick sort is {1000*(tend - tstart):.4f} ms")
        case 5:
            tstart = time.time()
            mergeSort(arr.copy(), 0, len(arr) - 1)
            tend = time.time()
            print(f"Time taken to sort {elements} elements using merge sort is {1000 * (tend - tstart):.4f} ms")
        case 6:
            A = to_heap_array(arr.copy())
            tstart = time.time()
            heapSort(A)
            tend = time.time()
            print(f"Time taken to sort {elements} elements using heap sort is {1000 * (tend - tstart):.4f} ms")
        case 7:
            threshold = int(input("Enter threshold: "))
            temp = arr.copy()
            tstart = time.time()
            mergeSortT(temp, 0, len(temp) - 1, threshold)
            tend = time.time()
            print(f"Time taken to sort {elements} elements using hybrid merge sort is {1000 * (tend - tstart):.4f} ms")
        case 8:
            k = int(input("Enter k to find kth smallest element: "))
            while k < 1 or k > elements:
                k = int(input(f"k must be between 1 and {elements}\nEnter k: "))
            result = kthSmallest(arr.copy(), 0, len(arr) - 1, k)
            print(f"The {k}th smallest element is {result}")
        case 9:
            break
