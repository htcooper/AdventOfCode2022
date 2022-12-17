# Open the input file in read-only mode
with open("input01.txt", "r") as file:
  # Initialize the current total and the top 3 totals to zero
  current_total = 0
  top_totals = [0, 0, 0]

  # Read each line of the file
  for line in file:
    # Remove leading and trailing whitespace from the line
    line = line.strip()

    # Check if the line is empty
    if line == "":
      # If the line is empty, save the current total and reset it to zero
      top_totals = sorted(top_totals + [current_total], reverse=True)[:3]
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

  # After reading all the lines, save the final total if it is one of the top 3
  top_totals = sorted(top_totals + [current_total], reverse=True)[:3]

# Output the sum of the top 3 totals
print(sum(top_totals))
