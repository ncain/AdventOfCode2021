with open('input.txt') as input:
  lines = [line.rstrip() for line in input.readlines()]

def naive_course():
  position = 0
  depth = 0
  for line in lines:
    direction, amount = line.split(' ')
    if direction == "forward":
      position += int(amount)
    elif direction == "down":
      depth += int(amount)
    elif direction == "up":
      depth -= int(amount)
  return position * depth

def clever_course():
  aim = 0
  position = 0
  depth = 0
  for line in lines:
    direction, amount = line.split(' ')
    if direction == "forward":
      position += int(amount)
      depth += (aim * int(amount))
    elif direction == "down":
      aim += int(amount)
    elif direction == "up":
      aim -= int(amount)
  return position * depth

print("Part one: " + str(naive_course()))
print("Part two: " + str(clever_course()))
