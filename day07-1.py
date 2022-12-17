from collections import defaultdict

with open('input07.txt') as f:

    # Container to hold current file path
    current_directory = []
    sizes = defaultdict(int)

    for line in f:
        
        # Update directory 
        if "$ cd" in line:
            linx, cmd, dir = line.split()
            
            # Go up a directory by removing last item from list
            if dir == "..":
                current_directory = current_directory[:-1]
            # Go down to new directory
            else:
                current_directory.append(dir) 
        
        # Ignore ls
        elif "$ ls" in line:        
            continue
        
        # If there is a numeric file size listed, update directory sizes
        else:                       
            size, name = line.split()
            
            # Check for a number
            if size.isnumeric():      
                for i in range(1, len(current_directory) + 1):

                    # Size of the file is added to the total size of the current directory in the sizes dictionary
                    sizes['/'.join(current_directory[0:i])] += int(size)

    # Filter values in the sizes dictionary to keep only those less than 100000 and sum values
    final_sum = sum(filter(lambda x: x < 100000, sizes.values()))
    print(final_sum)