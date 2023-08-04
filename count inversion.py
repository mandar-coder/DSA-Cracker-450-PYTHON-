#count inversion

def countinversion(arr, n):
    
    counti=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                counti+=1
    return counti

arr=[1,2,4,5]
n= len(arr)

print("count:", countinversion(arr,n))
