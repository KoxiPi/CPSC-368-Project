# CPSC 368 Final Project - Telehealth Trends Analysis

## Group Members
- Shenglong Chen
- Heather Lu
- Kaiwei Liu

## Research Questions
1. **(Shenglong)** How has telehealth use changed over time?  
   Specifically, is there a significant difference in the average percentage of telehealth users between the years 2020–2024?
2. **(Heather)** Are there any patterns between telehealth use and geographical location (Urban vs. Rural)?
3. **(Kaiwei)** How does the patient’s age impact telehealth use?

## Project Files

| Filename/Folder                             | Description |
|--------------------------------------------|-------------|
| `data/`                                     | Contains all raw and cleaned datasets used for analysis |
| `medicare_cleaned.csv`                      | Cleaned Medicare dataset with telehealth usage by year |
| `telemedicine_cleaned.csv`                  | Cleaned NCHS telemedicine usage dataset |
| `telemedicine_group_By_Age.csv`             | Grouped telemedicine data by age categories |
| `telemedicine_group_By_State.csv`           | Grouped telemedicine data by U.S. states |
| `telemedicine_group_National_Estimate.csv`  | National-level summary of telemedicine use |
| `Medicare_Telehealth_Trends_Q2_2024.csv`    | Original Medicare trends dataset |
| `Telemedicine_Use_in_the_Last_4_Weeks.csv`  | Original survey-based telehealth data |
| `medicare_cleaned.sql`                      | SQL queries used to clean and filter Medicare dataset |
| `telemedicine_groups.sql`                   | SQL used to aggregate telemedicine groups by age, state and national estimate |
| `EDAcode.ipynb`                             | Jupyter notebook for data analysis and visualizations |
| `dataCleaning.ipynb`                        | Jupyter notebook for preprocessing and cleaning raw data |
| `README.md`                                 | Project description and instructions (this file) |

---

## How to Run the Code

1. **Install Python** if you haven’t already.
2. Open the Jupyter notebooks in order:
   - `dataCleaning.ipynb` (first): Cleans raw datasets.
   - `EDAcode.ipynb` (second): Performs analysis, creates visualizations.
