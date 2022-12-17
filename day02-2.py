# initialize the total to 0
total = 0

# define a dictionary that maps each pair of letters to its corresponding value
letter_values = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7,
}

# open the input file for reading
with open('input02.txt') as file:
    # iterate over the lines in the file
    for line in file:
        # split the line into two letters
        letters = line.strip().split()
        
        # get the first letter
        first_letter = letters[0]
        
        # get the second letter
        second_letter = letters[1]
        
        # look up the value of the two letters in the dictionary and add it to the total
        total += letter_values[(first_letter, second_letter)]

# print the total
print(total)
