def raise_to_power(number,power):
    result=1
    for i in range(power):
        result*=number
    return result
number = int(input())
power = int(input())
print(raise_to_power(number,power))