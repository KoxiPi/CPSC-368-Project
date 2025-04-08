# CPSC 368 Final Project - Telehealth Trends Analysis

## Group Members
- Heather Lu
- Kaiwei Liu
- Shenglong Chen

## Research Questions
1. How has telehealth use changed over time? Specifically, is there a significant difference in the average percentage of telehealth users between the years 2020–2024?


2. Is there a significant difference in the average number of telehealth visits between rural and urban areas? How does usage vary across states?


3. Is there a significant difference in the frequency of telehealth use across different age groups? Are younger beneficiaries more likely to use telehealth than older ones?


## Project Files

| Filename/Folder                             | Description |
|--------------------------------------------|-------------|
| `data/medicare_cleaned.csv`                      | Cleaned Medicare dataset with telehealth usage by year |
| `data/telemedicine_cleaned.csv`                  | Cleaned NCHS telemedicine usage dataset |
| `data/telemedicine_group_By_Age.csv`             | Grouped telemedicine data by age categories |
| `data/telemedicine_group_By_State.csv`           | Grouped telemedicine data by U.S. states |
| `data/telemedicine_group_National_Estimate.csv`  | National-level summary of telemedicine use |
| `data/Medicare_Telehealth_Trends_Q2_2024.csv`    | Original Medicare trends dataset |
| `data/Telemedicine_Use_in_the_Last_4_Weeks.csv`  | Original survey-based telehealth data |
| `data/medicare_cleaned.sql`                      | SQL queries used to clean and filter Medicare dataset |
| `data/telemedicine_groups.sql`                   | SQL used to aggregate telemedicine groups by age, state and national estimate |
| `sqlFile/medicare_cleaned.sql`                      | Medicare dataset SQL file (with keys) ctually used in SQL plus  |
| `sqlFile/telemedicine_groups.sql`                   | Telemedicine groups SQL file (with keys) used used in SQL plus  |
| `EDAcode.ipynb`                             | Jupyter notebook for data analysis and visualizations |
| `dataCleaning.ipynb`                        | Jupyter notebook for preprocessing, cleaning raw data and generate the sql source file |
| `README.md`                                 | Project description and instructions (this file) |

---

## How to Run the Code

### Jupyter notebooks
1. **Install Python** if you haven’t already.
2. Open the Jupyter notebooks in order:
   - `dataCleaning.ipynb` (first): Cleans raw datasets.
   - `EDAcode.ipynb` (second): Performs analysis, creates visualizations.
   - (You may need to modify the file directory in your code to run it)

### SQL Plus
1. Use SSH to connect to remote.students.cs.ubc.ca using your CWL ID.
2. Upload 2 files in `sqlFile` folder to your SQL plus server.
3. Login in your account to the SQL plus server.
4. Query according to the SQL query command.
