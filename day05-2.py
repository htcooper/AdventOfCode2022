import re

crate_dict = {1: ['B','G','S','C'], 2: ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'], 3: ['M', 'Q', 'S'], 4: ['B','S','L','T','W','N','M'], 5:['J','Z','F','T','V','G','W','P'], 6:['C','T','B','G','Q','H','S'], 7:['T','J','P','B','W'], 8:['G','D','C','Z','F','T','Q','M'], 9:['N','S','H','B','P','F']}


# Read in the input file
with open('input05.txt') as f:
  
  # Iterate over each line in the file
  for line in f:
    # Extract the move instructions using a regular expression
    match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    num_items = int(match.group(1))
    from_crate = int(match.group(2))
    to_crate = int(match.group(3))

    # Check if the from_crate and to_crate keys exist in the crate dictionary
    if from_crate not in crate_dict:
      print(f'Error: Crate {from_crate} does not exist')
      continue
    if to_crate not in crate_dict:
      print(f'Error: Crate {to_crate} does not exist')
      continue

    # Move the specified number of items from one crate to another
    items_to_move = crate_dict[from_crate][-num_items:]
    crate_dict[from_crate] = crate_dict[from_crate][:-num_items]
    crate_dict[to_crate].extend(items_to_move)
    
  # Output the last element of each array in ascending order by key
  output = ''.join(str(crate_dict[key][-1]) for key in sorted(crate_dict))
  print(output)
