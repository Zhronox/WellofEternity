import csv

# Open the input file (text or XML)
input_file_path = r'your_input_file_path_here'
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

# Specify the keyword you want to search for
keyword = 'your_keyword_here'

# Initialize a list to store data
data_to_write = []

# Iterate through the lines
for line in lines:
    if keyword.lower() in line.lower():
        # Extract relevant information as needed
        relevant_info = line.strip()
        data_to_write.append([keyword, relevant_info])

# Specify the absolute path for the CSV file
output_csv_path = r'your_output_csv_file_path_here'

# Write data to the CSV file (replacing the old one)
with open(output_csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_write)

# Debugging output
print("CSV file replaced at:", output_csv_path)
print("Number of rows written to CSV:", len(data_to_write))
