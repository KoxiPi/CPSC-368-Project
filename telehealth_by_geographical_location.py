import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load Medicare dataset
medicare_df = pd.read_csv("/Users/heatherlu/Desktop/cpsc_368_Project/data/medicare_cleaned.csv")

# Filter for Rural and Urban
rural_df = medicare_df[medicare_df['Bene_RUCA_Desc'] == 'Rural']
urban_df = medicare_df[medicare_df['Bene_RUCA_Desc'] == 'Urban']

# Calculate mean telehealth visits
rural_mean = rural_df['Total_Bene_Telehealth'].mean()
urban_mean = urban_df['Total_Bene_Telehealth'].mean()

print(f"Average Rural Telehealth Visits: {rural_mean:.2f}")
print(f"Average Urban Telehealth Visits: {urban_mean:.2f}")

# Perform t-test
t_stat, p_val = ttest_ind(rural_df['Total_Bene_Telehealth'], 
                        urban_df['Total_Bene_Telehealth'], 
                        equal_var=False)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4e}")

# Load state-level telehealth usage dataset
tele_state_df = pd.read_csv("/Users/heatherlu/Desktop/cpsc_368_Project/data/telemedicine_group_By_State.csv")

# Group by state and calculate average usage
state_usage_avg = tele_state_df.groupby('State')['Value'].mean().sort_values(ascending=False)

# Bar plot
plt.figure(figsize=(14, 6))
state_usage_avg.plot(kind='bar', color='skyblue')
plt.title('Average Telehealth Usage by State (% using in last 4 weeks)')
plt.xlabel('State')
plt.ylabel('Average % Telehealth Use')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Display top and bottom 5 states
top_5 = state_usage_avg.head(5)
bottom_5 = state_usage_avg.tail(5)

print("Top 5 States by Average Telehealth Usage:\n", top_5)
print("\nBottom 5 States by Average Telehealth Usage:\n", bottom_5)

