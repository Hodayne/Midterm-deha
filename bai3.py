def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = list(map(int, input("Nhập mảng số nguyên (cách nhau bởi khoảng trắng): ").split()))
print("Mảng sau khi sắp xếp:", bubble_sort(arr))
