def bubleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [121, 87, 82, 11, 12, 45, 63, 56]

bubleSort(arr)
print(arr, "or\n")
for i in range(len(arr)):
    print("%d" % arr[i])
