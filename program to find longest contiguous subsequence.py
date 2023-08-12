#program to find longest contiguous subsequence

def findLongestConseqSubseq(arr, n):
    ans = 0
    count = 0

    # Sort the array
    arr.sort()

    v = []

    v.append(arr[0])

    # Insert repeated elements only
    # once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])

    # Find the maximum length
    # by traversing the array
    for i in range(len(v)):
        # Check if the current element is
        # equal to previous element +1
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
        # Reset the count
        else:
            count = 1
        # Update the maximum
        ans = max(ans, count)

    return ans

# Driver code
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    arr.append(element)

print("Length of the Longest contiguous subsequence is",
      findLongestConseqSubseq(arr, n))
#code by mandar
