arr = [5, 2, 8, 1, 9]

print("Original list:", arr)

# Linear Search
num = int(input("Enter number to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == num:
        print("Number found at index:", i)
        found = True
        break

if not found:
    print("Number not found")

# Bubble Sort
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted list:", arr)

# Binary Search
num = int(input("Enter number for binary search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == num:
        print("Number found at index:", mid)
        found = True
        break
    elif arr[mid] < num:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Number not found")