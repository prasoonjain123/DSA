def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1]<arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


bubbleSort([5,6,2,9,7,3])
bubbleSort(['idhf','wiuf','aedho','prasoon','prashant','pradeep'])