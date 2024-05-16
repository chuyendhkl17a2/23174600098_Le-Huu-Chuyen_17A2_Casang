def sumPdivisors(n):
    if n <= 1:
        return 0
    
    sum_divisors = 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors


number=36
print(f"Tổng các ước số chính của {number} là: {sumPdivisors(number)}")