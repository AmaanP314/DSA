#TRADITIONAL APPROACH TO WRITE FIBONNACI SERIES, HIGHLY INEFFICIENT, TC : O(2^n)
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

#USING DYNAMIC PROGRAMMING (TOP-DOWN APPROACH), EFFECTIVE ALGO., TC : O(2n - 1)

# memo = [None] * (100) #MEMOIZATION
# counter = 0
# def fib(n):
#     global counter
#     counter+=1
#     if memo[n] is not None:
#         return memo[n]
#     if n == 0 or n == 1:
#         return n
#     memo[n] = fib(n-1) + fib(n-2)
#     return memo[n]

# print(fib(7))
# print(counter)

#USING BOTTOME-UP APPROACH WITHOUT MEMOIZATION, TC : O(n - 1)

# counter = 0
# def fib(n):
#     fib_list = [0,1]
#     for i in range(2, n+1):
#         global counter
#         counter += 1
#         next_fib = fib_list[i-1] + fib_list[i-2]
#         fib_list.append(next_fib)
#     return fib_list[n]


# print(fib(100))
# print(counter)

#WITH MEMOIZAITON

# counter = 0
# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
    
#     if n <= 1:
#         return n
    
#     fib_list = [0, 1]
#     for i in range(2, n+1):
#         global counter
#         counter += 1
#         next_fib = fib_list[i-1] + fib_list[i-2]
#         fib_list.append(next_fib)
#         memo[i] = next_fib
    
#     return fib_list[n]

# # print(fib(100) * fib(200) * fib(300) * fib(400) * fib(500) * fib(600) * fib(700) * fib(800) * fib(900) * fib(1000))  
# print(fib(1000))
# print(counter)

from decimal import Decimal, getcontext

def compute_pi(num_decimals):
    """
    Compute pi using Gauss-Legendre algorithm to the specified number of decimal places.
    """
    getcontext().prec = num_decimals + 2
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)

    for _ in range(num_decimals):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    return pi

# Example usage
num_decimals = 10000  # Number of decimal places to compute
pi = compute_pi(num_decimals)
print(pi)



    
    
    