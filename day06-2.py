# open the file and read the line of characters
with open('input06.txt') as f:
  line = f.readline()

# initialize the index position to the 14th character
index = 13

# loop until a group of 14 contiguous characters that are all different is found
while index < len(line) - 1:
  # check if the previous 14 characters are all different
  if len(set(line[index-13:index+1])) == 14:
    # return the index position of the last character in the group
    print(index + 1)
    break
  else:
    # move to the next character and continue the loop
    index += 1
