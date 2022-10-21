from Stack import Stack
print("\nLets play Tower Of Hanoi !!")

stacks = []

#Creating three stacks for the game
left_stack = Stack("Left")
right_stack = Stack("Right")
middle_stack = Stack("Middle")

#Append each of the stacks into stacks array
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Setting up the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

#Keeps asking for a new input while num_disks is less than 3
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in reversed(range(1, num_disks + 1)):
    left_stack.push(i)
left_stack.print_items()

num_optimal_moves = pow(2 , num_disks) - 1

print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

def get_input():
    choices = [name.get_name()[0] for name in stacks] #Gets the first index of each name in the stacks array
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))
        user_input = input("")
        if user_input in choices:     #Checks whether the user_input in one of the elements in choices
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

#Playing the game
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.size == 0:
            print("\n\n\nInvalid Move. Try again")
        elif to_stack.size == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))




