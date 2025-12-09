# String Stuff
def is_palindrome(word):
    #checks is the argument word is a palindrome
    return word == word[::-1]


text = input("Fam pls enter a word: ")
if is_palindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is BORINGGG~")