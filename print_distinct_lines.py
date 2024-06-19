def print_distinct_lines(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Using a set to store distinct lines
    distinct_lines = set(lines)
    
    # Print the distinct lines
    for line in distinct_lines:
        print(line, end='')

# Example usage
input_file = 'FileHandling/smallfile.txt'
print_distinct_lines(input_file)
