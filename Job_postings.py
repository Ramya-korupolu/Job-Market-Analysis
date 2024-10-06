import pandas as pd
import random
from datetime import datetime, timedelta

# Define job-specific skills for a wider variety of job titles
skills_by_job = {
    "Data Analyst": ["Python", "SQL", "Tableau", "Excel"],
    "Data Scientist": ["Python", "R", "Machine Learning", "Statistics"],
    "Business Intelligence Analyst": ["SQL", "Power BI", "Data Warehousing", "Excel"],
    "Software Engineer": ["Java", "Python", "C++", "AWS"],
    "Front-End Developer": ["HTML", "CSS", "JavaScript", "React"],
    "Back-End Developer": ["Node.js", "Python", "SQL", "API Development"],
    "Full-Stack Developer": ["JavaScript", "React", "Node.js", "SQL"],
    "Product Manager": ["Agile", "Scrum", "Leadership", "Communication"],
    "Technical Product Manager": ["Agile", "Technical Writing", "API", "Software Development"],
    "Project Manager": ["Project Management", "Agile", "Risk Management", "MS Project"],
    "Digital Marketing Specialist": ["SEO", "Google Analytics", "Content Marketing", "PPC"],
    "SEO Analyst": ["SEO", "Keyword Research", "Google Analytics", "Backlink Analysis"],
    "Social Media Manager": ["Content Creation", "Facebook Ads", "Instagram", "Social Media Analytics"],
    "Financial Analyst": ["Excel", "Financial Modeling", "Forecasting", "Budgeting"],
    "Accountant": ["QuickBooks", "Tax Preparation", "Financial Reporting", "Excel"],
    "Investment Analyst": ["Financial Modeling", "Valuation", "Portfolio Management", "Excel"],
    "HR Manager": ["Recruitment", "Performance Management", "Employee Relations", "HRIS"],
    "Recruitment Specialist": ["Talent Sourcing", "Interviewing", "ATS", "Candidate Screening"],
    "Talent Acquisition": ["Recruitment", "Employer Branding", "Candidate Experience", "Negotiation"],
    "Customer Support Specialist": ["Customer Service", "CRM", "Communication", "Troubleshooting"],
    "Customer Success Manager": ["Account Management", "Client Relations", "Upselling", "CRM"]
}

companies = ["Google", "Microsoft", "Amazon", "Accenture", "Facebook", "Tesla", "Netflix", "Adobe", "IBM", "Salesforce"]
locations = ["San Francisco", "New York", "Seattle", "Remote", "Chicago", "Austin", "London", "Berlin", "Toronto", "Sydney"]
industries = ["Tech", "Healthcare", "Finance", "E-commerce", "Education", "Manufacturing", "Marketing", "Consulting"]
job_types = ["Full-Time", "Part-Time", "Internship", "Contract"]
experience_levels = ["Entry-level", "Mid-level", "Senior"]
salary_ranges = ["60k-80k", "80k-100k", "100k-120k", "120k-150k", "150k-200k"]

# Generate random dates for job postings from the last 3 years
def random_date():
    start_date = datetime.now() - timedelta(days=365 * 3)  # Start date is 3 years back
    random_days = random.randint(0, 365 * 3)  # Generate random days in the past 3 years
    return start_date + timedelta(days=random_days)

# Create a list to store the generated data
data = []

# Generate 500 synthetic job postings with expanded job-specific skills and random dates in the last 3 years
for _ in range(715):
    job_title = random.choice(list(skills_by_job.keys()))  # Select a random job title
    job = {
        "Job Title": job_title,
        "Company Name": random.choice(companies),
        "Required Skills": skills_by_job[job_title],  # Select 3 relevant skills
        "Location": random.choice(locations),
        "Industry": random.choice(industries),
        "Job Type": random.choice(job_types),
        "Experience Level": random.choice(experience_levels),
        "Posting Date": random_date().strftime('%Y-%m-%d'),
        "Salary Range": random.choice(salary_ranges)
    }
    data.append(job)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('job_postings_last_3_years.csv', index=False)
