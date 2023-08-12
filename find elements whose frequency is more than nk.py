# Python3 code to find elements whose
# frequency is more than n/k

def morethanNbyK(arr, n, k):
    x = n // k

    # unordered_map initialization
    freq = {}

    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    # Traversing the map
    for i in freq:
        # Checking if value of a key-value pair
        # is greater than x (where x=n/k)
        if freq[i] > x:
            # Print the key of whose value
            # is greater than x
            print(i)

# Driver code
if __name__ == '__main__':
    # Taking user input for array elements
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    n = len(arr)
    k = int(input("Enter the value of k: "))
    
    morethanNbyK(arr, n, k)
