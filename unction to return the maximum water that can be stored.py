# Function to return the maximum water that can be stored
def maxWater(arr, n):
    # To store the maximum water that can be stored
    res = 0

    # For every element of the array
    for i in range(1, n - 1):
        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1, n):
            right = max(right, arr[j])

        # Update the maximum water
        res = res + (min(left, right) - arr[i])

    return res

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    
    arr = []
    print("Enter the array elements:")
    for _ in range(n):
        element = int(input())
        arr.append(element)

    print("Maximum water that can be stored:", maxWater(arr, n))
