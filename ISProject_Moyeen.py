import pandas as pd
from datetime import datetime

                # Task:1 with advanced task start from here

          #Process Movie Data from Local CSV ('movies.csv')
file_path = 'movies.csv'  # Replace with the actual path of your movies.csv file

# Load the movie data from CSV
data = pd.read_csv(file_path)

# Extract Year from Title and Clean the Title
data['Year'] = data['title'].str.extract(r'\((\d{4})\)$')  # Extract the year from title
data['title'] = data['title'].str[:-7]  # Remove the year from the title column using string slicing

# Create a new DataFrame with MovieID, Title, and Year (First 10 Rows)
output_data = data[['movieId', 'title', 'Year']][:10]  # Select only the first 10 rows

# Save the processed data to a new CSV file
output_file = 'Moyeen_output.csv' # my output my name
output_data.to_csv(output_file, index=False)
print("Task 1: Movie data has been processed and saved to Moyeen_output.csv.")

                    # Task:1 is ended here






                # Task:2 with advanced task start from here

            #Process Monty Python Data from Online Source

url = 'http://pythonscraping.com/files/MontyPythonAlbums.csv'  # URL of the Montypythonalbum data
monty_data = pd.read_csv(url)  # Load the Monty Python album data

# Include the current date and time in a new column 'DateRetrieved'
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
monty_data['DateRetrieved'] = current_datetime

# Rename the 'Name' column to 'title'
monty_data.rename(columns={'Name': 'title'}, inplace=True)

# Add MovieID to Monty Python Data (Unique ID starting from the next available movieId)
if not output_data.empty:
    monty_data['movieId'] = range(output_data['movieId'].max() + 1, output_data['movieId'].max() + 1 + len(monty_data))
else:
    monty_data['movieId'] = range(1, len(monty_data) + 1)

# Combine the Monty Python data with the previous movie data
combined_data = pd.concat([output_data, monty_data], ignore_index=True)

# Rename the columns for better clarity
combined_data.rename(columns={'movieId': 'MovieId', 'title': 'Title', 'DateRetrieved': 'Date Retrieved'}, inplace=True)

# Save the combined data to the same CSV file
combined_data.to_csv(output_file, index=False)
print("Task 2: Monty Python album data has been appended and saved to Moyeen_output.csv.")

                     # Task:2 is ended here




                    # Task:3  start from here

# Add a Project Title to the Output CSV
title = "IS Project Python Task by Md Rafat Moyeen"  # Title to be added at the top of the output file

# Read the old content of the file (if it exists)
try:
    with open(output_file, 'r') as file:
        old_content = file.read()
except FileNotFoundError:
    old_content = ""  # If the file doesn't exist yet, no old content

# Open the file in write mode to overwrite with the title and old content
with open(output_file, 'w') as file:
    file.write(title + "\n\n")  # Write the project title and a blank line
    file.write(old_content)     # Write the old content back into the file

print(f"Final Step: The title '{title}' has been added to the first line of {output_file}.")

                 # Task:3 is ended here
