# Python3 program to find Maximum Product Subarray

# Returns the product of max product subarray.
def maxSubarrayProduct(arr, n):
    # Initializing result
    result = arr[0]

    for i in range(n):
        mul = arr[i]
        # traversing in current subarray
        for j in range(i + 1, n):
            # updating result every time
            # to keep an eye over the maximum product
            result = max(result, mul)
            mul *= arr[j]
        # updating the result for (n-1)th index.
        result = max(result, mul)

    return result

# Driver code
n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
    element = int(input("Enter element {}: ".format(i)))
    arr.append(element)

print("Maximum Subarray product is", maxSubarrayProduct(arr, n))
