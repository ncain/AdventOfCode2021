with open("input.txt") as input:
  lines = [int(line.rstrip()) for line in input.readlines()]

def count_increases(inlist, debug = False):
  count = 0
  for index, value in enumerate(inlist):
    if debug:
      print(str(value), end='')
    if index > 0 and value > inlist[index - 1]:
      count += 1
      if debug:
        print(" (increased)")
    elif index > 0 and value == inlist[index - 1] and debug:
      print(" (no change)")
    elif index > 0 and value <= inlist[index - 1] and debug:
      print(" (decreased)")
    elif index == 0 and debug:
      print(" (N/A - no previous sum)")
  return count

def sliding_window(inlist):
  outlist = list()
  for index, value in enumerate(inlist):
    if index + 2 < len(inlist):
      outlist.append(inlist[index] + inlist[index + 1] + inlist[index + 2])
  return outlist

print("Part one: " + str(count_increases(lines)))
print("Part two: " + str(count_increases(sliding_window(lines))))
