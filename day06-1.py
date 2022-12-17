# open the file and read the line of characters
with open('input06.txt') as f:
  line = f.readline()

# initialize the index position to the fourth character
index = 3

# loop until a group of 4 contiguous characters that are all different is found
while index < len(line) - 1:
  # check if the previous 4 characters are all different
  if len(set(line[index-3:index+1])) == 4:
    # return the index position of the last character in the group and correct for 0 indexing
    print(index + 1)
    break
  else:
    # move to the next character and continue the loop
    index += 1
