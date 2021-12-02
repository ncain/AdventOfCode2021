with open('input.txt') as input:
  lines = [line.rstrip() for line in input.readlines()]

def chart_course(naive = False):
  '''
  Compute the submarine's distance; if naive is true, aim is ignored and "up" and "down" move the submarine directly.
  '''
  position = 0
  depth = 0
  aim = 0
  for line in lines:
    direction, amount = line.split(' ')
    amount = int(amount)
    if direction == "forward":
      position += amount
      if not naive:
        depth += aim * amount
    elif direction == "down":
      aim += amount
    elif direction == "up":
      aim -= amount
  if naive:
    depth = aim
  return position * depth


print("Part one: " + str(chart_course(naive=True)))
print("Part two: " + str(chart_course()))
