with open("input.txt") as input:
  lines = [int(line.rstrip()) for line in input.readlines()]

count = 0
for index, value in enumerate(lines):
  if index > 0 and value > lines[index - 1]:
    count += 1
print(count)
