# Function to perform three-way partitioning
def threeWayPartition(arr, n, lowVal, highVal):
    # Initialize next available positions for smaller (than range) and greater elements
    start = 0
    end = n - 1
    i = 0

    # Traverse elements from left
    while i <= end:
        # If the current element is smaller than the range, put it on the next available smaller position.
        if arr[i] < lowVal:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1

        # If the current element is greater than the range, put it on the next available greater position.
        elif arr[i] > highVal:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1

        else:
            i += 1

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    
    arr = []
    print("Enter the array elements:")
    for _ in range(n):
        element = int(input())
        arr.append(element)

    lowVal = int(input("Enter the low value of the range: "))
    highVal = int(input("Enter the high value of the range: "))

    threeWayPartition(arr, n, lowVal, highVal)

    print("Modified array:")
    for i in range(n):
        print(arr[i], end=" ")
