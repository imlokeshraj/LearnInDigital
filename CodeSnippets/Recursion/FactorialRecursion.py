### Factorial By Recursion ###

def factorial(n):
	if n == 1:
		return 1
	else:
		return (n * factorial(n-1))

n=4
print("The Factorial of", n, "is", factorial(n))

### Lokesh Raj M | Learn in Digital ###