
def is_prime(num):
    counter = 0
    for i in range (1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2:
        return False
    elif counter == 1:
        return False
    else:
        return True
def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1

    return num

n = int(input())
print(get_next_prime(n))