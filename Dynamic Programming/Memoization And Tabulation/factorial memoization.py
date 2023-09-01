def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]

# Testing the factorial function
num = 5
print(f"The factorial of {num} is {factorial(num)}")