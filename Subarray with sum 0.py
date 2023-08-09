# Program to find if there is a zero sum subarray

def subArrayExists(arr, N):
    # Traverse through array and store prefix sums
    n_sum = 0
    s = set()

    for i in range(N):
        n_sum += arr[i]

        # If prefix sum is 0 or it is already present
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)

    return False

# Drive function
n = int(input("Array size: "))  # Convert input to integer
arr = []  # Initialize an empty list to store elements

print("Enter elements:")
for i in range(n):
    element = int(input())  # Convert input to integer
    arr.append(element)  # Add the element to the list

# Function call
if subArrayExists(arr, n):
    print("Found a subarray with 0 sum")
else:
    print("No such subarray exists!")
