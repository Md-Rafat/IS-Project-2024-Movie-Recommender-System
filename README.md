# IS_Project_Movie_Recommender_System

## Project Overview

**Project Title**: IS_Project_Movie_Recommender_System  

IS project documentation is a major part of data analysis and visualization course offered by IMIS at South Westphalia University of applied science. We have been provided four movie datasets, and the project task is divided into three parts: 
 Developing a movie recommender system using KNIME
 Creating a Power BI dashboard based on KNIME solution or movie dataset
 Introductory and advanced level python tasks


## Objectives

1. **Developing movie recommender system in KNIME Analytics Platform**: Create movie recommender system by using different algorithms and methods in KNIME using the movies.csv & ratings.csv dataset.
2. **Creating a Power BI dashboard**: Create a well organised Power BI dashboard by highlighting key aspects by using IMDB_movie_dataset.csv.
3. **Introductory and advanced level python tasks**: Solve three seperate python tasks within PythonAnywhere by using both movies.csv file & MontyPythonAlbums.csv file.



## Project Structure

### 1. KNIME - Developing a Movie Recommender System in KNIME Analytics Platform

- **Recommendation System Based on Association Rule Learner**: An Association Rule Learner is a machine learning algorithm that is used to discover interesting relationships (associations) between variables in large datasets. It is also known as market basket analysis. One of the important applications of association rule learner is it recommends products, movies, songs etc. based to the user’s previous behavior or content.

**Workflow Description**:

 ![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/67cbc06064e5f9f8ac4d1c67a3769624848673d3/Screenshot1.png)

The above workflow consists of three major parts: data input and preprocessing, transformation and output which will be shown by another picture later. Here in the workflow, it is shown that I use two datasets (movies and ratings) based on the significance of the columns. In the first layer of the workflow my objective is to create a separate column for the year by extracting the year from the title column of the dataset. So, after loading the movies.csv into CSV Reader, I use string manipulation node and Excel Writer node to extract the number (year). Then, I load the extracted year data into Excel Reader and assign a new CSV Reader node for my second dataset which is ratings.csv. In the second layer, with the help of Row Filter I clean the dataset by removing some irrelevant or unwanted rows based on row id, because I find some rows containing title in the year column as well as a range of numeric values. In the third layer, I inner joined both the extracted movies.csv node and rating.csv node with the help of Joiner node while the Join column is movie id. After that, for the missing value, if there is any, I use Missing Value node, and the Missing Value node is connected to the Column Filter node to ensure cleaned data is processed further. Column Filter node removes unnecessary columns such as timestamp, imdbId etc. to focus on relevant data. Then, in Cell Splitter I select genres column to split and for resorting the column I use Column Resorter node. Then, I introduce Association Rule Learner node, there my transactions column is genres split, Min support = 0.01 and Min confidence = 0.01. once the Association Rule Learner node is executed, it outputs the Association Rules in a data table. These association rules are considered frequent and strong according to the support and confidence that I specified. Finally, I filter only the top 30 strongest rules-based confidence and support using the Top K Selector node. 

**Results and Outputs**:

![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/2daadfe8cae2567779355b6427de9c237f5a179d/Screenshot2.png)

As it can be seen in the Top K Selector node (Top 30 strongest rules) output data table after the execution that, the last three columns – Consequent, implies and items contain the rule itself. Items column contains an antecedent. The implies column indicates the direction. Consequent column contains the recommended genre. From the above figure we can see one rule where Mystery movie genre is the antecedent and Thriller genre is the consequent; the confidence is 0.712 which means about 71.2% user who watches Mystery genre will also be interested to watch Thriller genre movie. The information can be used to recommend the specific genre or type of movies to the future users. 


- **Recommendation System Based on K Nearest Neighbors (KNN)**: K-Nearest Neighbors (KNN) is a simple, yet effective machine learning algorithm used for both classification and regression tasks. K-Nearest Neighbor is very easy to use, and it is very effective to apply in any recommender system.

**Workflow Description**:

![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/d221758d628af3ce77e7c590e654687517056922/Screenshot3.png)

The KNIME workflow between the recommendation system based on K Nearest Neighbors (KNN) and the recommendation system based on Association Rule Learner has some similarities. I use the same dataset in the K Nearest Neighbor workflow and use the same year extraction technique as well as some Row Filter to remove the unwanted rows. Then, after using Joiner node and Missing Value node this time I use String to Number node to change the data type of the ‘Year’ column. Then I use Rule Engine node to specify some rules based on rating. In the Rule Engine node, I specify two rules with the help of given functions there. The rules are Ratings 0 - 2.5 = not recommended and Ratings 3 - 5 = recommended. In the Rule Engine node, I append the column Recommendation. I use Column Filter here as well to remove unnecessary columns like timestamp, imdbId etc. After that, I use Partitioning node to divide my data into training data and test data. I choose the size of my first partition or training data 80% and second partition or test data 20% and select Random sampling. Then, I drag K Nearest Neighbor node and connect it with the partitioning node. In the K Nearest Neighbor node, I select my class column = Recommendation, Number of neighbors = 25 and marked Weight neighbours by distance. In the last layer of my workflow I drag a new Joiner node and join the classified output data of K Nearest Neighbor node and Excel Reader node of movies.csv (with extracted year), the purpose of using this Joiner node is to bring the title column back in the output data table for better understanding of the recommendation system which I removed previously in the Column Filter node because using non numeric column in the K Nearest Neighbor is not possible. In addition, I use Column Filter and Column Resorter accordingly to remove unnecessary columns and resorting the columns. Finally, I use a Scorer node to determine the accuracy status, correct classified data or wrong classified data. In the configuration of Scorer node, I select Recommendation column as my first column and Class [KNN] column as my second column. After the execution, I select view: Confusion Matrix option from there I found the total accuracy is 82.25% and error is 17.75% and among the total 20000 predicted class of data, 16450 are correctly classified and 3550 are wrong classified. 

**Confusion Matrix - Scorer**

![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/713e2c1040fb2278a7aba65fc7397f359955c485/Screenshot4.png)


### 2. Power BI - Creating a Power BI dashboard by using IMDB_movie_dataset.csv

For my Power BI dashboard creation, I chose a different dataset which is named imdb_movie_dataset.csv. I downloaded the dataset from Kaggle.com. After that I do some transformation work and make few measures and finally create a dashboard with some highlighted insights from the dataset. 

**Transformation Phase**:
1.	I find the rating column data type is a whole number and the rating are a mixer of in a scale of 100 and 10. So at first, I change the data type from whole number to decimal number and apply a mathematical transformation using Power BI's built-in field calculations, use the divide by 10 options from the standard field.
2.	I had to replace some values in the rating column from whole number to decimal number even after changing the data type
3.	The genres and actors were more than one, most of the movies so I use split column and unpivot columns filter to split them based on the same movie rank

**Creating New Measures**:
I created five measures in the formula bar by writing DAX formula, which are given below:
1.	Avg Metascore = AVERAGE(imdb_movie_dataset[Metascore])
2.	Avg Rating = AVERAGE(imdb_movie_dataset[Rating])
3.	Avg Runtime = AVERAGE(imdb_movie_dataset[Runtime (Minutes)])
4.	Avg Votes = AVERAGE(imdb_movie_dataset[Votes])
5.	Total Movies = COUNT(imdb_movie_dataset[Rank])

**Dashboard Analysis**:
I use two separated pages to create the power BI dashboard with some key insights from the analysis. I highlighted all the measures which I have been created in the earlier steps in the dashboard. From where my notable findings are, total movies = 838, Avg rating of the movies = 6,81, Avg runtime = 114,64 minutes, Avg metascore = 59,58 and Avg votes = 193,23k

![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/24b5950eef43a1765a40a603a26e989f77e05dcd/Screenshot5.png)
![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/1424daca75aed6f1907364a42869842d9fdeef4a/Screenshot6.png)


The most highlighting elements from the dashboard page- 1 are: average rating of top 50 movies in the basis of revenue – The dark knight has got the highest rating of 9. Inception holds the second place with the rating of 8,8. Then, in the total number of movies by year chart, it is notable that year 2016 had the highest number of movies of 198, 2015 had 109 and the lowest was in 2006 with only 41 movies. In the clustered column chart the title total number of movies by rating shows that, the maximum number of movie ratings fall in the range between 6 to 8 and the highest 43 movies hold the rating of 7. 
Now, some notable factors of dashboard page -2 are: Average rating by genre in the pie chart indicates that, war genre movie has the highest average rating of 7,60 and the lowest average rating is horror genre movie with the rating of 6,29. The chart of top 20 actors based on the total number of movies highlights that, Christian Bale and Mark Wahlberg both have 11 movies and they are the top of the list. In the total movies by genre chart, I find an interesting fact that, drama genre movie has the highest number of 419 movies however, if we compare this genre by average rating, we can find the average rating of drama genre movie is 7,04 which is not even in the top five rating list. Lastly, I use a decomposition tree to show the total movies by directors and their casted actors, where the director Ridley Scott has directed 8 movies and he casted the actor Russell Crowe twice and director David Yates has directed 6 movies and his notable casted actors are Ruper Grint and Daniel Radcliffe, they both acted under David Yates four times. 


### 3. Python - Solve three seperate python tasks within PythonAnywhere by using both movies.csv file & MontyPythonAlbums.csv file.

1. **Read the first ten movies from the movies.csv file and write them to a new csv file called yoursurname_output.csv, your output should only include the MovieID and Title, not genre. Advanced task - remove year from the title column and place it in a new column called year**:

```python
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

```

2. **Read a file from the following online source -http://pythonscraping.com/files/MontyPythonAlbums.csv and append it to the end of your output file. Included in your output needs to be the actual date and time that your program ran to retrieve the data. Advanced task - Assign and include a movieid attribute in the output 
which continues from where the previous data ended (i.e. movies.csv movieid 1-10)**:

```python
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

```

3. **Prompt the user to enter a title for the output file and write this as the first line in your output file, to be followed by a blank line**:

```python
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

```

## Conclusion

In conclusion, this project provided a valuable opportunity to gain hands-on experience with tools such as KNIME, Power BI, and Python. It enhanced my ability to research various techniques and methodologies, fostering the development of innovative analytical ideas

## Author - Md Rafat Moyeen

This project is part of my portfolio, showcasing the KNIME, Power BI & Python skills essential for data analyst roles.

### LinkedIn Profile

- **LinkedIn**: [Connect with me professionally](https://www.linkedin.com/in/mdrafatm)
- **Email**:    (moyeenmdrafat@gmail.com)

Thank you and I look forward to connecting with you!
