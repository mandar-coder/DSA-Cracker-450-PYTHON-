# Program to display the Fibonacci series

# Function to generate and print the Fibonacci series
def fibo(a):
    m, n = 0, 1
    count = 0

    # Check if the input is valid
    if a <= 0:
        print("Alert!")
    elif a == 1:
        print(f"Fibonacci: {m}")
    else:
        print("Fibonacci:", end=" ")

    # Generate and print the Fibonacci series
    while count < a:
        count += 1
        print(m, end=" ")
        nth = m + n
        m = n
        n = nth

# Get user input for the number of Fibonacci numbers to display
a = int(input("How many numbers do you want to display: "))
fibo(a)

# Code by Mandar
