def has_overlap(range1, range2):
  start1, end1 = range1
  start2, end2 = range2
  return (start1 <= end2 and end1 >= start2)

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
    # Check if the ranges have an overlap
    if has_overlap((start1, end1), (start2, end2)):
      count += 1
  print(count)