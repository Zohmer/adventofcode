#Position in 2d space x is horisontal positioning and y is depth
position = [0, 0]

data = open('./input', 'r')
instructions = data.read()
instructions = instructions.split("\n")

for i in instructions:
    command = i.split(" ")
    if command[0] == "forward":
        position[0] += int(command[1])
    elif command[0] == "up":
        position[1] -= int(command[1])
    elif command[0] == "down":
        position[1] += int(command[1])

print("Submarine position is: " + str(position[0]) + ", " + str(position[1]))
result = position[0] * position[1]
print("Multiplied they are: " + str(result))