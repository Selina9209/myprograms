# # place = int(input("ENTER N:  "))

# # def fin(num):
# #     fib_0 = 0
# #     fib_1 = 1
# #     interger = 0
# #     while interger < place:
# #         fib_0 = fib_1
# #         fib_1 = fib_0 + fib_1
# #         interger=+1
# #     return(fib_1)


# # if fin(place) == place:
# #     print(fin(place))


#     def fib(nth):
#     if nth in {0,1}:
#         return nth
#     else:
#         location = 2
#         two_before = 0
#         one_before = 1
#         total_sum = 0
#         while location <= nth:
#             total_sum = two_before + one_before
#             two_before = one_before
#             one_before = total_sum
#             location += 1

#         return total_sum
num = 1
total = 0

while num <= 10:
	total = total + num
	num = num + 1

print(total)