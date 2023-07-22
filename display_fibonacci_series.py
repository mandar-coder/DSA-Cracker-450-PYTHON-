#display_fibonacci_series
def fibo(a):
	m,n = 0,1
	count = 0
	if a<=0:
		print("Alert!")
	elif a == 1:
		print(f"fibonaci:{m}")
	else:
		print(f"fibonaci: ",end=" ")
	while count < a:
		count +=1
		print (m, end=" ")
		nth = m+n
		m=n 
		n = nth
a= int(input("How Many no u want to display:"))
fibo(a)
