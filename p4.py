# Factors of a Number

# start = 1
# end = int(input("Enter a number: "))
# factor_count = 0
# while start <= end:
#     result = end/start
#     if end % start == 0:
#         print(f"{end} has a factor of {start}")
#         factor_count += 1
#     start = start +1
# print(f"{end} has {factor_count} factors.")
# if factor_count == 2:
#     print(f"{end} is a prime number.")
# else:
#     print(f"{end} is a composite")

# # Better way?

import math
start = 1
num = int(input("Enter a value: "))

new_stop = int(math.sqrt(num))+1

while start < new_stop:
    if num%start == 0:
        divided = num//start
        if start != divided:
            factor_count += 2
        else:
            factor_count += 1
    start += 1
print(f"{num} has {factor_count} mamy factors.")