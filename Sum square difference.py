sum_1=0
sum_2=0
for i in range(1, 101):
    sum_1 += i**2
print (sum_1)

print ("break")
for z in range (1, 101):
    sum_2 += z
print ((sum_2**2))
    
result = sum_2 - sum_1
print (result)
    
