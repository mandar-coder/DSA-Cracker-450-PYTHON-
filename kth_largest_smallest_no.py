#find kth largest element
def kth(arr,n,k):
    arr.sort()
    print(arr[k-1])

arr=[1,32,11,23,16,33]
k = int(input("No:"))
n = len(arr)
kth(arr,n,k)