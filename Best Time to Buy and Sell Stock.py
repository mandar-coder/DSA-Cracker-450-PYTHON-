#Best Time to Buy and Sell Stock

def maxprofit(arr, n):
    buy = arr[0]
    max = 0
    for i in range(1,n):
        if(buy>arr[i]):
            buy = arr[i]
        elif(arr[i]-buy>max):
            max = arr[i]-buy
    return max
    
arr = [7, 1, 5, 6, 4]
n= len(arr)
print("max profit", maxprofit(arr,n))