# Initialize variable to hold total
total = 0

# Assign values to letters 'a' through 'z' and 'A' through 'Z'
letter_values = {chr(i): i-96 for i in range(97, 123)}  # a-z
letter_values.update({chr(i): i-38 for i in range(65, 91)})  # A-Z

# Open input file
with open('input03.txt') as f:
  # Create a dictionary where the key is the line number and the value is the set of letters
    letter_sets = {i: set(line.strip()) for i, line in enumerate(f)}

# Iterate through the dictionary in groups of 3
for i in range(0, len(letter_sets), 3):
    set1 = letter_sets.get(i, set())
    set2 = letter_sets.get(i+1, set())
    set3 = letter_sets.get(i+2, set())

    # Find the intersection of the three sets
    intersection = set1 & set2 & set3

    # Add the sum of the values of the letters in the intersection to the total
    total += sum(letter_values[letter] for letter in intersection)

print(total)
