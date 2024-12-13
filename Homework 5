import math

def find_min_angle_point(x1, x2, y1, y2, z1, z2):

    points = [(x1, x2), (y1, y2), (z1, z2)]
    min_angle = float('inf')
    min_point = None

    for x, y in points:
        if x == 0 and y == 0: 
            continue
        angle = math.atan2(y, x)
        if abs(angle) < min_angle:
            min_angle = abs(angle)
            min_point = (x, y)

    return min_point



x1, x2 = 1, 1
y1, y2 = 2, 0
z1, z2 = -1, 1

min_point = find_min_angle_point(x1, x2, y1, y2, z1, z2)
if min_point:
    print(f"Точка с минимальным углом: {min_point}")
else:
    print("Все точки совпадают с (0,0)")



def find_palindrome_primes(n):
    
    

    def is_prime(num):
       
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(binary_string):
        
        return binary_string == binary_string[::-1]

    palindrome_primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            binary = bin(i)[2:]  
            if is_palindrome(binary):
                palindrome_primes.append(i)
    return palindrome_primes

n = 100
result = find_palindrome_primes(n)
print(f"Простые числа, являющиеся палиндромами в двоичной системе, не превосходящие {n}: {result}")
