num1 = int(input('Enter any integer number: '))
count = 0
num = num1

while num1 != 0:
    num1 //= 10
    count += 1

max_digit = 0
max_index = 0
min_digit = 9
min_index = 0

for i in range(count):
    digit = (num % 10**(count - i)) // 10**(count-1-i)
    if digit > max_digit:
        max_digit = digit
        max_index = i
    if digit < min_digit:
        min_digit = digit
        min_index = i
result = min_digit * 10**(count - 1) + max_digit

j = 0
r = 2
b = 1

while r != count:
    digit = (num % 10**(count - j)) // 10**(count-1-j)
    if (digit == min_digit + b or digit == min_digit) and j != min_index:
        result += digit * 10**(count - r)
        r += 1
    j += 1
    if j == count:
        j = 0
        b += 1

print(result)