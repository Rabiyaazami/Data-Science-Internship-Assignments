import pandas as pd

df = pd.read_csv("kerala.csv")

# Basic exploration
print(df.info())
print(df.describe())

# Step 2: Create new DataFrame with boolean flags
df['JUN_GT_500'] = df['JUN'] > 500
df['JUL_GT_500'] = df['JUL'] > 500
df['FLOODS'] = df[['JUN', 'JUL']].max(axis=1) > 500  # Consider flood if either Jun or Jul > 500

new_df = df[['YEAR', 'JUN_GT_500', 'JUL_GT_500', 'FLOODS']]
print(new_df.head())

# Step 3-6: Probabilities
p_flood_given_june = (new_df['FLOODS'] & new_df['JUN_GT_500']).sum() / new_df['JUN_GT_500'].sum()
p_june_given_flood = (new_df['FLOODS'] & new_df['JUN_GT_500']).sum() / new_df['FLOODS'].sum()
p_flood_given_july = (new_df['FLOODS'] & new_df['JUL_GT_500']).sum() / new_df['JUL_GT_500'].sum()
p_july_given_flood = (new_df['FLOODS'] & new_df['JUL_GT_500']).sum() / new_df['FLOODS'].sum()

print(f"Probability of flood given June > 500mm: {round(p_flood_given_june, 4)}")
print(f"Probability of June > 500mm given flood: {round(p_june_given_flood, 4)}")
print(f"Probability of flood given July > 500mm: {round(p_flood_given_july, 4)}")
print(f"Probability of July > 500mm given flood: {round(p_july_given_flood, 4)}")
