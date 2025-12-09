# String Checklist
# Create an empty string
empty_string = ""
ver2 = ''
# Determind if the string is empty
    # method 1
if not str_var:
    print("The string is empty")

if len(str_var) == 0:
    print("String is empty")

#Formatting a String to contain dynamic Data
name = "Fluffington"
str_var = f"Hello {name}!"

# Acess indivudal characters/item in a string
print(name[0])
print(name[-2])
# Access the first, acces the last item in a string
print(name[0])
print(len(name)-1)
print(name[-1])

#Join two/multiple strings together
a = "poo"
b = "poo"
c = a + b
print(c) #expect poopoo

# Reverse a string
temp = "park"
reversed_temp = temp[::-11]
v2 = ''.join(reversed(temp))

# Create a copy of a string
temp = "hyrdoflask"
tempcopy = temp[:]
another_copy = temp

# Compare strings for equality 
a = "marshall"
b = "dog"
status = a == b # i think false

# Determine the minimum and maximum value within a string
temp = "hydroflask"
print(max(temp))
print(min(temp))
print(max("hello", "goodbye"))
print(min("1", "2", "3"))

# Determine if an item or a pattern exist within a string
word = "poopooplatter"
if "poo" in word:
    print("THERE IS POO!")

# Locate the index of an item or a pattern within a string
poop_Location = word.find("poo")
poop_Location = word.index("poop")

# Count how often an item or a pattern occurs within a string
poop_count = word.count("poo")

# Convert all item in. a string to uppercase/lowercase (upper and lower you can put nothing in the bracket)
yell_hydroflask = "hydroflask".upper()
calm_hydroflash = yell_hydroflask.lower()

# Determine if the string can be converted to an interger
# Convert a string to an interger
str_num = "67"
num = 0
if str_num.isdigit():
    num = int(str_num)

# Determine if a string only contains alphabetical characters
word = "shsm".isalpha()

# Remove non alphabetical chartacters from a string
    #Sometimes.... it is reasier to create/grow than remove
gibberish = "!283y 40eqi!dcHJDSFByhujiko4r56yhjk"
clean = ""
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1

# Remove all alphabetical chartacters from a string
gibberish = "!283y 40eqi!dcHJDSFByhujiko4r56yhjk"
clean = ""
i = 0
while i < len(gibberish):
    if gibberish[i].isalpha() == False:
        clean += gibberish[i]
    i += 1

gibberish = "!283y 40eqi!dcHJDSFByhujiko4r56yhjk"
clean = ""
i = 0
while i < len(gibberish):
    if not gibberish[i].isalpha():
        clean += gibberish[i]
    i += 1

# Remove all whitespaces from a string
example = " h e l l o o o o o o f h he h e hee                lo"
example = exmaple.replace(" ", "")

# Sort a string in ASCII order or reverse-ASCII order

# Determine if a string follows a ruleset
