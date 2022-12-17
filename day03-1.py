
# Initialize a variable to hold the total
total = 0

# Assign values to letters 'a' through 'z' and 'A' through 'Z'
values = {chr(i): i - 96 for i in range(ord('a'), ord('z')+1)}
values.update({chr(i): i - 38 for i in range(ord('A'), ord('Z')+1)})

# Open the input file
with open('input03.txt') as f:
  # Iterate over each line of the input file
  for line in f:
    # Split the line into two sets
    first_half = set(line[:len(line)//2])
    second_half = set(line[len(line)//2:])

    # Find the intersection of the two sets
    intersection = first_half & second_half

    # Add the values of the characters in the intersection to the total
    for char in intersection:
      total += values[char]

# Output the total
print(total)