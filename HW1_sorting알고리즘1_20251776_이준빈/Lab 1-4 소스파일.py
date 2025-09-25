def selectionSort(list):
    for i in range(len(list)-1, 1, -1):
        max_idx = i
        for j in range(i):
            if list[max_idx] < list[j]:
                max_idx = j
        list[i], list[max_idx] = list[max_idx], list[i]

list = [64, 25, 12, 22, 11]
print("Original list = %s" % list)

selectionSort(list)

print("Sorted list by Selection method")
print(list)