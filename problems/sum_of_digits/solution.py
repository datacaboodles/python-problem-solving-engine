number = abs(int(input()))
total = 0

while number > 0:
    total += number % 10
    number //= 10

print(total)

# or 
# ALTERNATIVE WAY (FOR INTERVIEW FLEXIBILITY)
# Yes, convert the number to a string and sum the characters 
number = input()
total = 0

for ch in number:
    if ch != '-':
        total += int(ch)

print(total)

