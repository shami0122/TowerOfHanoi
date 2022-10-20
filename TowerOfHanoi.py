from Stack import Stack
print("\nLets play Tower Of Hanoi !!")

stacks = []

#Creating three stacks for the game
left_stack = Stack("Left")
right_stack = Stack("Right")
middle_stack = Stack("Middle")

#Append each of the stacks into stacks array
stacks.append(left_stack)
stacks.append(right_stack)
stacks.append(middle_stack)

#Setting up the game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

