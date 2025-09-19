# # Heads or Tails

# from random import choice # choice is a function that randomly chooses from a list

# while True:
#     print("Welcome to our heads or tails game!")
#     print("People choose either heads or tails")
#     while True:
#         user_input = input("User's choice:  ")
#         user_input = user_input.lower() #this makes everything lowercase

#         if user_input in {"heads", "tails", "head", "tail"}: 
#             # user_input was valid, we can exit the infintie loop
#             break # allows us to exit a looping structure
#         else:
#             print("Please type in heads or tails. :)")
#     # end of while
#     flip_result = choice(["heads", "tails"])

#     print(f"The computer flipped: {flip_result}.")
#     if user_input in {"heads", "head"} and flip_result == "heads":
#         print("The user guessed CORRECTLY!")
#     elif user_input in {"tails" , "tail"} and flip_result == "tails":
#         print("The user guessed CORRECTLY!")
#     else: 
#         print("awww....... ")
#     user_input = input("Want to stop gamblings? yes/no: ")
#     if user_input.lower() == "yes":
#         break

#snacks and lanterns

place = 1

while True:
    dice = int(input("Input your dice roll:  "))

    if dice > 6:
        print("girl...")
    elif dice < 1:
        print("girl...")
    else:
        place = place+dice
        game_dict = {
            9 : 34,
            54 : 19,
            40 : 64,
            90 : 48,
            67 : 86,
            99 : 77
        }
        if place in game_dict:
            square = game_dict[place]
            print(place)
            
        else:
            print(place)
        # if place == 40:
        #     place = 64
        #     print(f"You're at {place}")
        # elif place == 9:
        #     place = 34
        #     print(f"You're at {place}")
        # elif place == 67:
        #     place = 86
        #     print(f"You're at {place}")
        # elif place == 54:
        #     place = 19
        #     print(f"You're at {place}")
        # elif place == 90:
        #     place = 48
        #     print(f"You're at {place}")
        # elif place == 99:
        #     place = 77
        #     print(f"You're at {place}")
        # else:
        #     print(f"You're at {place}")
    
    if place == 100:
        print(f"GUESS WHAT!! YOU'RE ON {place}")
        break
    if place > 100:
        place = place - dice
        print(f"You're at {place}")