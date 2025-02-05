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

 ![Image Alt](https://github.com/Md-Rafat/IS_Project_Movie_Recommender_System/blob/67cbc06064e5f9f8ac4d1c67a3769624848673d3/Screenshot1.png)

The above workflow consists of three major parts: data input and preprocessing, transformation and output which will be shown by another picture later. Here in the workflow, it is shown that I use two datasets (movies and ratings) based on the significance of the columns. In the first layer of the workflow my objective is to create a separate column for the year by extracting the year from the title column of the dataset. So, after loading the movies.csv into CSV Reader, I use string manipulation node and Excel Writer node to extract the number (year). Then, I load the extracted year data into Excel Reader and assign a new CSV Reader node for my second dataset which is ratings.csv. In the second layer, with the help of Row Filter I clean the dataset by removing some irrelevant or unwanted rows based on row id, because I find some rows containing title in the year column as well as a range of numeric values. In the third layer, I inner joined both the extracted movies.csv node and rating.csv node with the help of Joiner node while the Join column is movie id. After that, for the missing value, if there is any, I use Missing Value node, and the Missing Value node is connected to the Column Filter node to ensure cleaned data is processed further. Column Filter node removes unnecessary columns such as timestamp, imdbId etc. to focus on relevant data. Then, in Cell Splitter I select genres column to split and for resorting the column I use Column Resorter node. Then, I introduce Association Rule Learner node, there my transactions column is genres split, Min support = 0.01 and Min confidence = 0.01. once the Association Rule Learner node is executed, it outputs the Association Rules in a data table. These association rules are considered frequent and strong according to the support and confidence that I specified. Finally, I filter only the top 30 strongest rules-based confidence and support using the Top K Selector node. 


### 2. Data Exploration & Cleaning

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
