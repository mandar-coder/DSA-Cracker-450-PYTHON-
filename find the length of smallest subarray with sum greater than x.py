# Function to find the length of smallest subarray with sum greater than x
def smallestSubWithSum(arr, n, x):
    # Initialize length of smallest subarray as n+1
    min_len = n + 1

    # Pick every element as the starting point
    for start in range(0, n):
        # Initialize sum starting with the current start
        curr_sum = arr[start]

        # If the first element itself is greater
        if curr_sum > x:
            return 1

        # Try different ending points for the current start
        for end in range(start + 1, n):
            # Add the last element to the current sum
            curr_sum += arr[end]

            # If the sum becomes more than x and the length of
            # this subarray is smaller than the current smallest
            # length, update the smallest length (or result)
            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)
        
    return min_len

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    
    arr = []
    print("Enter the array elements:")
    for _ in range(n):
        element = int(input())
        arr.append(element)
