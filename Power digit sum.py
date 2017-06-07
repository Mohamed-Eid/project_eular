number = 2**1000
string_number = str(number)
sum_of_digits = 0

for i in string_number:
    sum_of_digits =sum_of_digits + int(i)
    
print("Sum of all digits:", sum_of_digits)
