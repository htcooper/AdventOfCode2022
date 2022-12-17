# Open the input file in read-only mode
with open("input01.txt", "r") as file:
  # Initialize the current total and the largest total to zero
  current_total = 0
  largest_total = 0

  # Read each line of the file
  for line in file:
    # Remove leading and trailing whitespace from the line
    line = line.strip()

    # Check if the line is empty
    if line == "":
      # If the line is empty, save the current total and reset it to zero
      largest_total = max(largest_total, current_total)
      current_total = 0
    else:
      # If the line is not empty, try to convert it to a number
      try:
        number = int(line)
      except ValueError:
        # If the line cannot be converted to a number, skip it
        continue

      # Add the number to the current total
      current_total += number

  # After reading all the lines, save the final total if it is the largest seen so far
  largest_total = max(largest_total, current_total)

# Output the largest total
print(largest_total)

