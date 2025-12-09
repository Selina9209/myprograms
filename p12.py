# thing = input("Wee: ")
# uppercase = ""
# digits = 0
# for x in thing:
#     if x.isalpha():
#         if x.isupper():
#             uppercase+=x
#     elif x.isdigit():
#         x = int(x)
#         digits = digits + x


# print(uppercase+ str(digits))


def cleaner(text):
    # Text kinda looks like cG23mH-9s
    # we want GH14
    upper_case = ""
    positive = ""
    negative = ""
    total_sum = 0
    for item in text:
        if item.isalpha() and item.isupper():
            upper_case += item
            if len(positive) > 0:
                total_sum += int(positive)
                positive = ""
            if len(negative) > 0:
                total_sum += int(negative)
                negative = ""
        elif item == "-":
            if len(negative) > 0:
                total_sum += int(negative)
                negative = "-"
            else:
                negative = "-"
        elif item.isdigit():
            if len(negative) > 0:
                negative += item
            else:
                positive += item

    #end 
    if len(positive) > 0:
        total_sum += int(positive)

    if len(negative) > 0:
        total_sum += int(negative)

    product_code = upper_case + str(total_sum)
    return product_code 


inp = input("input: ")

print(cleaner(inp))
