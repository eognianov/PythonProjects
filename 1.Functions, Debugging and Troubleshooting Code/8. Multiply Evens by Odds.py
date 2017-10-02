def get_multiple_of_even_and_odds(n):
    return get_sum_of_even_digits(n) * get_sum_of_odd_digits(n)

def get_sum_of_even_digits(n):
    result = 0
    while n != 0:
        result += n % 10 if (n % 10)% 2==0 else 0
        n //= 10
    return result

def get_sum_of_odd_digits(n):
    result = 0
    while n != 0:
        result += n % 10 if (n % 10)% 2==1 else 0
        n //= 10
    return result

print(get_multiple_of_even_and_odds(abs(int(input()))))