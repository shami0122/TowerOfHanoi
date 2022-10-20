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

for i in reversed(range(num_disks)):
    left_stack.push(i)

num_optimal_moves = pow(2 , num_disks) - 1

print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

def get_input():
    choices = [name.get_name()[0] for name in stacks] #Gets the first index of each name in the stacks array
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))


