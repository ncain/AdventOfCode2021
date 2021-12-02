with open('input.txt') as input:
  lines = [line.rstrip() for line in input.readlines()]

horizontal = 0
depth = 0
for line in lines:
  direction, amount = line.split(' ')
  if direction == "forward":
    horizontal += int(amount)
  elif direction == "down":
    depth += int(amount)
  elif direction == "up":
    depth -= int(amount)

print(horizontal * depth)

