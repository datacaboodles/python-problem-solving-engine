number = int(input())
number = abs(number)

reversed_number = 0

while number > 0:
    last_digit = number % 10
    reversed_number = reversed_number * 10 + last_digit
    number = number // 10

print(reversed_number)

# Another way to solve this 
num = int(input())
sign = -1 if num < 0 else 1
num = abs(num)

reversed_num = int(str(num)[::-1])

print(sign * reversed_num)
