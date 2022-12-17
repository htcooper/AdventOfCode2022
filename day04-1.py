def fully_contained(range1, range2):
  start1, end1 = range1
  start2, end2 = range2
  return (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1)

# Open the input file
with open('input04.txt') as f:

  count = 0
  # Iterate over each line in the file
  for line in f:
    # Split the line into the two ranges
    range1, range2 = line.strip().split(',')
    # Split each range into start and end values
    start1, end1 = map(int, range1.split('-'))
    start2, end2 = map(int, range2.split('-'))
    # Check if one range is fully contained by the other
    if fully_contained((start1, end1), (start2, end2)) or fully_contained((start2, end2), (start1, end1)):
      count += 1
  print(count)
