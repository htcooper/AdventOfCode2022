# initialize the total to 0
total = 0

# define a dictionary that maps each letter to its corresponding value
letter_values = {'A': 1, 'X': 1, 'B': 2, 'Y': 2, 'Z': 3, 'C': 3}

# open the input file for reading
with open('input02.txt') as file:
    # iterate over the lines in the file
    for line in file:
        # split the line into two letters
        letters = line.strip().split()
        
        # get the value of the first letter
        first_letter_value = letter_values[letters[0]]
        
        # get the value of the second letter
        second_letter_value = letter_values[letters[1]]
        
        # if the values of the two letters are equal, add 3 to the total
        # plus the value of the second letter
        if first_letter_value == second_letter_value:
            total += 3 + second_letter_value
        
        # if the value of the first letter is 1 more than the value of the second letter
        # or if the value of the first letter is 2 less than the value of the second letter,
        # add 0 to the total plus the value of the second letter
        elif first_letter_value == second_letter_value + 1 or first_letter_value == second_letter_value - 2:
            total += 0 + second_letter_value
        
        # if the value of the first letter is 1 less than the value of the second letter
        # or if the value of the first letter is 2 more than the value of the second letter,
        # add 6 to the total plus the value of the second letter
        elif first_letter_value == second_letter_value - 1 or first_letter_value == second_letter_value + 2:
            total += 6 + second_letter_value

# print the total
print(total)
