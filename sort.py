import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0] 
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot] 
    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    test_cases = [
        [5, 3, 8, 1, 2, 7],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [4, 4, 4, 4, 4, 4, 4]
    ]

    for test in test_cases:
        print("Original List:", test)
        sorted_list = bubble_sort(test)
        print("Bubble Sorted:", sorted_list)
        sorted_list = quick_sort(test)
        print("Quick Sorted:", sorted_list)
    
    mylist = [random.randint(1, 100) for _ in range(10)]
    print("Original List:", mylist)
    
    print("Bubble Sorted:", bubble_sort(mylist.copy()))
    
    mylist = [random.randint(1, 100) for _ in range(10)]
    print("Quick Sorted:", quick_sort(mylist.copy()))

if __name__ == "__main__":
    main()
