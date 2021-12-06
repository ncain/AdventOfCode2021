from typing import List

with open('input.txt') as input:
  lines = [line.rstrip() for line in input.readlines()]

def power_consumption(diagnostic: List[str], debug: bool = False) -> int:
  '''
  Given a list of bit strings, produce the submarine's power consumption.
  The gamma rate is found by counting the bits in each position of the diagnostic input.
  The most common bit in each position is the value in that position of the gamma rate.
  The epsilon rate is found by the same process but using the least-common bit;
  consequently, the epsilon rate is the bitwise negation of the gamma rate.
  The submarine's power consumption is the product of the epsilon and gamma rates.

  Assumptions:
    1. The length of the bit strings is static; that is, shorter values will be padded with zeroes.
  '''
  gamma = 0
  epsilon = 0
  width = len(diagnostic[0])
  for i in range(width):
    count = 0  # the number of set bits in each bit position as we traverse the diagnostic list
    for record in diagnostic:
      if record[i] == '1':
        count += 1
    if count > len(diagnostic) / 2:  # this might need to be >=; ties are ambiguous
      gamma |= 1 << (width - i - 1)  # because i is in a range, we have to correct by 1
    else:
      epsilon |= 1 << (width - i - 1)
  if debug:
    print("Gamma:   " + format(gamma, '012b') + " (" + str(gamma) + ")")
    print("Epsilon: " + format(epsilon, '012b') + " (" + str(epsilon) + ")")
  return gamma * epsilon


def life_support_rating(diagnostic: List[str], debug: bool = False) -> int:
  '''
  Get the life support rating
  '''
  def rating(diagnostic, oxygen: bool, debug) -> int:
    '''
    Get either the oxygen generator or CO2 scrubber rating, depending on the bit criterion.
    If oxygen is True, get Oxygen. Otherwise, get CO2.
    '''
    working_set = diagnostic.copy()
    width = len(diagnostic[0])
    for i in range(width):
      if len(working_set) == 1:
        return int(working_set[0], 2)
      if len(working_set) < 1:
        raise ValueError('Working set is empty!')
      search_hits = list()
      count = 0
      for record in working_set:
        if record[i] == '1':
          count += 1
      for record in working_set:
        if count >= len(working_set) / 2:  # then 1 is the most common value in position i, or 1 and 0 are equally common
          if (oxygen and record[i] == '1') or (not oxygen and record[i] == '0'):
            search_hits.append(record)
        else:  # then 0 is strictly the most common value in position i
          if (oxygen and record[i] == '0') or (not oxygen and record[i] == '1'):
            search_hits.append(record)
      working_set = search_hits.copy()
  oxygen = rating(diagnostic, True, debug)
  carbon = rating(diagnostic, False, debug)
  return oxygen * carbon


if __name__ == "__main__":
  print("Power consumption: " + str(power_consumption(lines)))
  print("Life support: " + str(life_support_rating(lines, True)))
