n = int(input("Enter the number of terms for the Fibonacci sequence: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms:")
    for _ in range(n):
        print(a, end=" ")  # Print the current term
        a, b =b, a + b    # Update the terms for the next iteration
