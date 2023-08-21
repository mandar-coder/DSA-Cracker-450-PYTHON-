import sys

class GFG:

    # Function for finding the minimum number of swaps
    # required to bring all the numbers less
    # than or equal to k together.
    @staticmethod
    def minSwap(arr, n, k):
        # Initially snowBallsize is 0
        snowBallSize = 0
        i = 0
        while (i < n):
            # Calculating the size of window required
            if (arr[i] <= k):
                snowBallSize += 1
            i += 1

        swap = 0
        ans_swaps = sys.maxsize
        i = 0
        while (i < snowBallSize):
            if (arr[i] > k):
                swap += 1
            i += 1
        ans_swaps = min(ans_swaps, swap)

        i = snowBallSize
        while (i < n):
            # Checking in every window no. of swaps
            # required and storing its minimum
            if (arr[i - snowBallSize] <= k and arr[i] > k):
                swap += 1
            elif (arr[i - snowBallSize] > k and arr[i] <= k):
                swap -= 1
            ans_swaps = min(ans_swaps, swap)
            i += 1

        return ans_swaps

    @staticmethod
    def main(args):
        print("Minimum Swaps to Arrange Elements Less Than or Equal to k Together")
        
        n = int(input("Enter the number of elements: "))
        arr = []
        print(f"Enter {n} elements:")
        for _ in range(n):
            arr.append(int(input()))

        k = int(input("Enter the value of k: "))
        
        result = GFG.minSwap(arr, n, k)
        print(f"Minimum swaps required: {result}")

if __name__ == "__main__":
    GFG.main([])
