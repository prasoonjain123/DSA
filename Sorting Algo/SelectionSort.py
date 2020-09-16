# By setting the min of array at start
def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

selectionSort([5,6,2,9,7,3])
selectionSort(['idhf','wiuf','aedho','prasoon','prashant','pradeep'])