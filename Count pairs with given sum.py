#Count pairs with given sum
def countpairs(arr, n):
    count = 0
    pair= 6
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j] == pair):
                count+=1
    return count

arr = [1,5,1,7]
n = len(arr)
print("Output", countpairs(arr,n));
