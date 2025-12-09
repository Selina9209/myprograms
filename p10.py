# def clean(text):
#     result = ""
#     i = 0 #avoid using the word Index as it is a function/method name
#     while i < len(text):
#         #.isalpha() returns True if the given chracter is 
#         # alphabetical
#         if text[i].isalpha():
#             result = result + text[i].lower()
#         i += 1
#     # end of while loop
#     return result

# hehe = input("hehe: ")
# print(clean(hehe))

# # Linear Search
# def str_lin_search(text, target):
#     if not text: #len(text) == 0
#         return -1
#     else:
#         i = 0
#         while i < len(text):
#             if text[i] == target:
#                 return i
#             i += 1 
#         #end of while loop
#         return -1
# print("Jasper... Where is p?", str_lin_search("Jasper", "p"))

# #only find the very first occurance
# #linear search, search algorithm 

# def anagram1(one):
#     x = one.lower
#     x = sorted(x)

# def anagram2(two):
#     y = two.lower
#     y = sorted(y)

# oe = input(": ")
# tw = input(": ")

# oe = anagram1(oe)
# tw = anagram2(tw)
# if oe == tw:
#     print('truw')
# else:
#     print("false")

def alpha_sorting(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0
    while i < len(abc):
        # if abc[i] in text.lower():
        #     result += abc[i]*(text.lower().count(abc[i]))
        current_letter = abc[i]
        text_lowered = text.lower()
        if current_letter in text_lowered:
            letter_count = text.lower().count(current_letter)
            result = result + (current_letter * letter_count)
        i += 1
    return result 