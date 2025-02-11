from math import *
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        sqrt_d = sqrt(d)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        roots_min = min(x1, x2)
        roots_max = max(x1, x2)
    elif d == 0:
        x3 = (-b) / (2 * a)
        return x3, x3
    return roots_min, roots_max

a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)