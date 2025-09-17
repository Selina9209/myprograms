# Dounts
donut_count = int(input("Enter the number of donuts: "))
events = int(input("Enter the number of events: "))

# we stop when no donuts or no events
current_event = 1 # PERSONALLY MR PARK DOES 0
while current_event <= events and donut_count >= 0:
    event_type = input("+ or -?: ")
    donut_amount - int(input("Enter donut amount: "))
    if event_type == "+":
        donut_count = donut_count + donut_amount
    elif event_type == "-":
        donut_count = donut_count - donut_amount
    else:
        print("Invalid input")

# end of while
print(f"At the end of our events, we have {donut_count} donuts.")