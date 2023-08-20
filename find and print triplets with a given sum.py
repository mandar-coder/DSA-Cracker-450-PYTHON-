# Function to find and print triplets with a given sum
def find3Numbers(A, arr_size, sum):
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):
        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):
            # Now look for the third number
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    # Triplet found, print the triplet and return True
                    print("Triplet is", A[i], ", ", A[j], ", ", A[k])
                    return True
    # If we reach here, then no triplet was found
    return False

# Driver program
A = []  # Initialize an empty list for array elements
arr_size = int(input("Enter the size of the array: "))
print("Enter the array elements:")
for _ in range(arr_size):
    element = int(input())
    A.append(element)
sum = int(input("Enter the desired sum: "))

if find3Numbers(A, arr_size, sum):
    print("Triplet with the given sum exists.")
else:
    print("No triplet with the given sum found.")
