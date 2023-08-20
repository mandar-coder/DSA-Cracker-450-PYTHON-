# Function to find the minimum difference between
# maximum and minimum values of chocolate distribution
def findMinDiff(arr, n, m):
    # If there are no chocolates or number
    # of students is 0
    if m == 0 or n == 0:
        return 0

    # Sort the given packets
    arr.sort()

    # Number of students cannot be more than
    # the number of packets
    if n < m:
        return -1

    # Initialize the minimum difference
    min_diff = arr[n - 1] - arr[0]

    # Find the subarray of size m such that
    # the difference between the last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the number of packets: "))
    
    arr = []
    print("Enter the sizes of packets:")
    for _ in range(n):
        element = int(input())
        arr.append(element)

    m = int(input("Enter the number of students: "))

    result = findMinDiff(arr, n, m)
    if result != -1:
        print("Minimum difference is", result)
    else:
        print("Number of students cannot be more than the number of packets.")
