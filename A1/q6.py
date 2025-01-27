import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]
prime_numbers = [num for num in numbers if is_prime(num)]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Prime numbers:", prime_numbers)
