n = 100
f = 1
while n > 1 :
    f = f * n
    n -= 1
print (f)

number = f
string_number = str(number)
sum_of_digits = 0

for i in string_number:
    sum_of_digits =sum_of_digits + int(i)
    
print("Sum of all digits:", sum_of_digits)

