# implementation to check
# if an array is PalinArray or not

# Function to check if palindrome or not
def isPalindrome(N):
	str1 = "" + str(N)
	len1 = len(str1)
	for i in range(int(len1 / 2)):
		if (str1[i] != str1[len1 - 1 - i]):
			return False
	return True

# Function to check
# if an array is PalinArray or not
def isPalinArray(arr, n):
	
	# Traversing each element of the array
	# and check if it is palindrome or not
	for i in range(n):
		ans = isPalindrome(arr[i])
		if (ans == False):
			return False
	return True
	
# Driver code
if __name__ == '__main__':
	
	arr = [ 121, 131, 20 ]
	
	# length of array
	n = len(arr)
	res = isPalinArray(arr, n)
	if (res == True):
		print("Array is a PalinArray")
	else:
		print("Array is not a PalinArray")
