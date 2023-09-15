MOD = 1405695061

def generate_k_markov(k, N):
    base = [1 for _ in range(k)]
    
    markov_numbers = set(base)
    queue = [base]

    while queue:
        solution = queue.pop(0)
        
        for i in range(k):
            new_solution = solution.copy()
            new_solution[i] = k * prod_except_i(solution, i) - sum_except_i(solution, i)
            
            new_solution = sorted(new_solution)

            if all([val > 0 for val in new_solution]) and max(new_solution) <= N:
                if tuple(new_solution) not in queue:
                    queue.append(new_solution)
                    for num in new_solution:
                        markov_numbers.add(num)
                        
    return sum(markov_numbers) % MOD

# Use caching for these functions
prod_cache = {}
sum_cache = {}

def prod_except_i(arr, i):
    if tuple(arr + [i]) in prod_cache:
        return prod_cache[tuple(arr + [i])]
    
    prod = 1
    for j, val in enumerate(arr):
        if j != i:
            prod *= val
            
    prod_cache[tuple(arr + [i])] = prod
    return prod

def sum_except_i(arr, i):
    if tuple(arr + [i]) in sum_cache:
        return sum_cache[tuple(arr + [i])]
    
    s = sum(arr) - arr[i]
    sum_cache[tuple(arr + [i])] = s
    return s

def S(K, N):
    total = 0
    for k in range(3, K+1):
        total += generate_k_markov(k, N)
        total %= MOD
    return total

print(S(10**18, 10**18))
