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







- **Record Count**: Determine the total number of records in the dataset.
- **Customer Count**: Find out how many unique customers are in the dataset.
- **Category Count**: Identify all unique product categories in the dataset.
- **Null Value Check**: Check for any null values in the dataset and delete records with missing or null values.

```sql
SELECT COUNT(*) FROM Retail_Sales;
SELECT COUNT (transactions_id) AS total_sale FROM Retail_Sales;
SELECT COUNT(DISTINCT customer_id) FROM Retail_Sales;
SELECT DISTINCT category FROM Retail_Sales;

SELECT * FROM Retail_Sales
WHERE 
    transactions_id IS NULL OR sale_date IS NULL OR sale_time IS NULL OR customer_id IS NULL OR 
    gender IS NULL OR age IS NULL OR category IS NULL OR quantity IS NULL OR
    price_per_unit IS NULL OR cogs IS NULL OR total_sale IS NULL;

DELETE FROM retail_sales
WHERE 
    transactions_id IS NULL OR sale_date IS NULL OR sale_time IS NULL OR customer_id IS NULL OR 
    gender IS NULL OR age IS NULL OR category IS NULL OR quantity IS NULL OR
    price_per_unit IS NULL OR cogs IS NULL OR total_sale IS NULL;
```

### 3. Data Analysis & Findings

The following SQL queries were developed to answer specific business questions:

1. **Write a SQL query to retrieve all columns for sales made on '2022-11-05**:
```sql
SELECT *
FROM Retail_Sales
WHERE sale_date = '2022-11-05';
```

2. **Write a SQL query to retrieve all transactions where the category is 'Clothing' and the quantity sold is more than 4 in the month of Nov-2022**:
```sql
SELECT 
  *
FROM Retail_Sales
WHERE 
    category = 'Clothing'
    AND 
    TO_CHAR(sale_date, 'YYYY-MM') = '2022-11'
    AND
    quantity >= 4
```

3. **Write a SQL query to calculate the total sales (total_sale) and total number of orders for each category.**:
```sql
SELECT 
    category,
    SUM(total_sale) AS net_sale,
    COUNT(transactions_id) AS total_orders
FROM Retail_Sales
GROUP BY category
```

4. **Write a SQL query to find the average age of customers who purchased items from the 'Beauty' category.**:
```sql
SELECT
    ROUND(AVG(age), 2) as avg_age
FROM Retail_Sales
WHERE category = 'Beauty'
```

5. **Write a SQL query to find all transactions where the total_sale is greater than 1000.**:
```sql
SELECT * FROM Retail_Sales
WHERE total_sale > 1000
```

6. **Write a SQL query to find the total number of transactions (transaction_id) made by each gender in each category.**:
```sql
SELECT 
    category,
    gender,
    COUNT(transactions_id) AS number_of_transactions
FROM Retail_Sales
GROUP BY 
    category,
    gender
ORDER BY category, gender

```

7. **Write a SQL query to calculate the average sale for each month. Find out best selling month in each year**:
```sql
SELECT 
       year,
       month,
    avg_sale
FROM 
(    
SELECT 
    EXTRACT(YEAR FROM sale_date) AS year,
    EXTRACT(MONTH FROM sale_date) AS month,
    AVG(total_sale) AS avg_sale,
    RANK() OVER(PARTITION BY EXTRACT(YEAR FROM sale_date) ORDER BY AVG(total_sale) DESC) as rank
FROM Retail_Sales
GROUP BY 1, 2
) as table_1
WHERE rank = 1
```

8. **Write a SQL query to find the top 5 customers based on the highest total sales **:
```sql
SELECT 
    customer_id,
    SUM(total_sale) AS total_sales
FROM Retail_Sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5
```

9. **Write a SQL query to find the number of unique customers who purchased items from each category.**:
```sql
SELECT 
    category,    
    COUNT(DISTINCT customer_id) AS unique_customer
FROM Retail_Sales
GROUP BY category
```

10. **Write a SQL query to create each shift and number of orders (Example Morning <12, Afternoon Between 12 & 17, Evening >17)**:
```sql
WITH shift_sale
AS
(
SELECT *,
    CASE
        WHEN EXTRACT(HOUR FROM sale_time) < 12 THEN 'Morning'
        WHEN EXTRACT(HOUR FROM sale_time) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS shift
FROM Retail_Sales
)
SELECT 
    shift,
    COUNT(transactions_id) AS Orders    
FROM shift_sale
GROUP BY shift
```

## Findings

- **Customer Demographics**: The dataset includes customers from various age groups, with sales distributed across different categories such as Clothing and Beauty.
- **High-Value Transactions**: Several transactions had a total sale amount greater than 1000, indicating premium purchases.
- **Sales Trends**: Monthly analysis shows variations in sales, helping identify peak seasons.
- **Customer Insights**: The analysis identifies the top-spending customers and the most popular product categories.
  

## Conclusion

This project serves as a comprehensive introduction to SQL for data analysts, covering database setup, data cleaning, exploratory data analysis, and business-driven SQL queries. The findings from this project can help drive business decisions by understanding sales patterns, customer behavior, and product performance.


## Author - Md Rafat Moyeen

This project is part of my portfolio, showcasing the SQL skills essential for data analyst roles.

### LinkedIn Profile

- **LinkedIn**: [Connect with me professionally](https://www.linkedin.com/in/mdrafatm)
- **Email**:    (moyeenmdrafat@gmail.com)

Thank you and I look forward to connecting with you!
