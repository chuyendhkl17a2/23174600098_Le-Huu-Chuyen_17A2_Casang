import math

def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)
def combinations(n, r):
    return permutations(n, r) // math.factorial(r)

n = 5
r = 3
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là: {permutations(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: {combinations(n, r)}")