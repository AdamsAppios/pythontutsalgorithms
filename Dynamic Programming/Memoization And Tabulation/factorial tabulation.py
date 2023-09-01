def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    fact_table = [0] * (n+1)
    fact_table[0] = fact_table[1] = 1
    
    for i in range(2, n+1):
        fact_table[i] = i * fact_table[i-1]
    
    return fact_table[n]

# Testing the factorial function
num = 5
print(f"The factorial of {num} is {factorial(num)}")