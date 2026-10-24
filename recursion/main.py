from functools import lru_cache, wraps
import time
import timeit


def timer(func):
    depth = 0  # shared by all recursive calls of this one decorated original function

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        is_top_level = depth == 0
        depth += 1

        if is_top_level:
            start = time.perf_counter()

        result = func(*args, **kwargs)  # call original fib

        depth -= 1

        if is_top_level:
            end = time.perf_counter()
            print(f"{func.__name__} took {end - start:.6f} seconds")

        return result
    return wrapper


# def function(counter):
#     # print current counter's value, define base & recursive cases, propagate base case value up
#     print(counter)
#     if counter > 3:  # base case
#         return "Job Done!"

#     return function(counter + 1)  # recursive case


# print(function(0))

# ============================
# FACTORIAL
# ============================

# def factorial_iter(number):
#     # accumulate resulting product, e.g. 1 * 2 * 3... n!
#     if number < 0:
#         raise ValueError("Not defined for negative numbers")
#     if number == 0:
#         return 1

#     # 5! -> 1 * 2 * 3 * 4 * 5 = ?
#     result = 1
#     for num in range(1, number + 1):  # 1 -> 5
#         result *= num

#     return result


# print(factorial_iter(9))


# def factorial_recursive(number):
#     """Time O(n), Space O(n)-call stack depth"""
#     if number < 0:
#         raise ValueError("Not defined for negative numbers")

#     if number < 2:
#         return 1  # base case

#     return number * factorial_recursive(number - 1)  # recursive case


# print(factorial_recursive(5))

# ============================
# FIBONACCI SEQUENCE
# ============================

# def fib_iterative(number):
#     # 1, 1, 2, 3, 5, 8, 13, 21, 34..
#     a, b = 1, 1
#     for _ in range(2, number):
#         a, b = b, a + b
#     return b


# print(fib_iterative(7))


# def fib_recursive(number):
#     if number <= 0:
#         return 0
#     elif number == 1:
#         return 1
    
#     return fib_recursive(number - 1) + fib_recursive(number - 2)


# print(fib_recursive(5))


# def fib_memo(number, memo=None):
#     if memo is None:
#         memo = {}

#     # get from cache
#     if number in memo:
#         return memo[number]

#     # base case
#     if number <= 0:
#         return 0
#     elif number == 1:
#         return 1

#     memo[number] = fib_memo(number - 1, memo) + fib_memo(number - 2, memo)

#     return memo[number]


# print(fib_memo(20))


# @lru_cache(maxsize=None)
# def fib_cached(n):
#     if n <= 1:
#         return n
#     return fib_cached(n - 1) + fib_cached(n - 2)


# print(fib_cached(20))


# def memoize(func):
#     cache = {}
#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result
#     return wrapper


# @memoize
# # @timer
# def fibonacci(num):
#     if num <= 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fibonacci(num - 1) + fibonacci(num - 2)


# print(fibonacci(20))


# print(
#     timeit.timeit(
#         "fibonacci(40)",
#         setup="""from __main__ import fibonacci""",
#         number=100000
#     )
# )
