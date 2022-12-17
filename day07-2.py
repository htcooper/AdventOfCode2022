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

    root_dir_size = sizes['/']
    remaining_space = 70000000 - root_dir_size
    needed_space = 30000000 - remaining_space

    # Return list of dictionary items whose size is greater than the remaining space and then sort ascending
    dir_list = [(k,v) for k, v in sizes.items() if v > needed_space]
    dir_list = sorted(dir_list, key = lambda x: x[1])

    print(dir_list[0])



    