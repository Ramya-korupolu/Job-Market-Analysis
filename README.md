# Job-Market-Analysis

## Overview
This project analyzes the job market to uncover in-demand skills, job roles, industries, and locations based on job postings.
We have used a combination of **Python (Jupyter Notebook)** for data manipulation and **Power BI** for visualization. 
The analysis focuses on:
- Identifying the top in-demand skills across various industries.
- Understanding the most sought-after job roles.
- Determining the industries offering the most opportunities.
- Comparing job postings based on different locations.
- Assessing salary distribution based on experience level.

We also provide an interactive **Power BI Dashboard** to explore these insights.

### Tools Used:
- **Python (Pandas, Seaborn)**: For data cleaning, exploration, and analysis.
- **Power BI**: For creating interactive visualizations and dashboards.



## Analysis in Jupyter Notebook
The data cleaning and initial analysis were conducted in **Jupyter Notebook** using **Python** libraries like Pandas, Matplotlib, and Seaborn.

### Key Steps in Jupyter Notebook:
1. **Data Cleaning**: 
   - Handled missing values, formatted columns (e.g., extracting `Year` from `Posting Date`).
   - Cleaned the `Required Skills` column and exploded the list of skills into individual rows for easier analysis.

2. **Top Skills Analysis**:
   - Identified the top in-demand skills using Pandas and visualized them using Matplotlib and Seaborn.

3. **Job Role Analysis**:
   - Analyzed the most common job roles in the dataset.
   
4. **Salary Analysis**:
   - Calculated average salaries by experience level and visualized the findings.
  
## Visualizations in the Power BI Report
The Power BI report includes the following visualizations:

- **Top In-Demand Skills**: A bar chart highlighting the most requested skills in job postings.
- **Top 10 In-Demand Job Roles**: A vertical bar chart displaying the most frequent job titles.
- **Industry Proportions**: A pie chart showing the industry distribution of job postings.
- **Filter by Location**: An interactive filter to drill down job postings by city.
- **Filter by Experience Level**: Allows users to filter job postings by required experience.
- **Filter by Year**: A dynamic filter to explore how the demand for roles has changed over time.


## Key Insights
1. **Top Skills**: Python, SQL, and Excel are among the most sought-after skills across multiple industries.
2. **Job Roles**: Data Analyst and Software Engineer are consistently in high demand.
3. **Salary Trends**: Senior roles offer significantly higher salaries than entry-level positions.
4. **Geographic Trends**: The tech industry is concentrated in cities like San Francisco and New York, while remote jobs are growing.


## Conclusion
The analysis provided insights into the current job market trends, focusing on skills, roles, industries, and locations. Through the combination of Python for data analysis and Power BI for visualization, this project enables both in-depth analysis and user-friendly exploration of job market data.


