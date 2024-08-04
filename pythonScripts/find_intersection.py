# Define the file paths
file1_path = 'file1.txt'
file2_path = 'file2.txt'
output_file_path = 'intersection.txt'

# Read lines from the first file
with open(file1_path, 'r') as file1:
    lines_file1 = set(file1.readlines())

# Read lines from the second file
with open(file2_path, 'r') as file2:
    lines_file2 = set(file2.readlines())

# Find the intersection of the lines
intersection_lines = lines_file1.intersection(lines_file2)

# Write the intersected lines to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(intersection_lines)

print(f'Intersection of lines written to {output_file_path}')
