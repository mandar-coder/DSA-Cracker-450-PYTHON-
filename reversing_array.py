#reversing no by recursion method
#reversing function

def reverse(A,start,end):
    if start>=end:
        return
    A[start],A[end] = A[end],A[start];
    reverse(A,start+1,end-1)


A = [1,2,3,4,5,6]
print(A)

reverse(A,0,5)
print(A)
