# 📦 Common Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ───────────────────────────────────────────────────────────────
# Problem Statement 1: Spotify Top 50 Dataset Analysis
# ───────────────────────────────────────────────────────────────

print("🔹 Problem 1: Spotify Top 50 Songs Analysis")

# Step 1: Load dataset
spotify_df = pd.read_csv("https://www.dropbox.com/s/2hg67jin2n852mz/top50spotify.csv?dl=1")

# Step 2: Drop the first column and save to 'top50.csv'
spotify_df.drop(spotify_df.columns[0], axis=1, inplace=True)
spotify_df.to_csv('top50.csv', index=False)

# Step 3: Average Energy and Length of first 10 songs
avg_energy = spotify_df.head(10)['Energy'].mean()
avg_length = spotify_df.head(10)['Length.'].mean()
print(f"Average Energy (first 10): {avg_energy:.2f}")
print(f"Average Length (first 10): {avg_length:.2f}")

# Step 4: Total length of songs grouped by genre
length_by_genre = spotify_df.groupby('Genre')['Length.'].sum().sort_values(ascending=False)
print("\nTotal length by genre:\n", length_by_genre)

# Step 5: Artist with most tracks in one genre
grouped = spotify_df.groupby(['Artist.Name', 'Genre']).size().reset_index(name='Count')
most_tracks = grouped.sort_values('Count', ascending=False).iloc[0]
print(f"\nArtist with most tracks in a genre: {most_tracks['Artist.Name']} ({most_tracks['Count']} tracks in {most_tracks['Genre']})")

# Step 6: Tracks by that artist
tracks_by_artist = spotify_df[spotify_df['Artist.Name'] == most_tracks['Artist.Name']]
print("\nTracks by that artist:\n", tracks_by_artist[['Track.Name', 'Genre']])

# ───────────────────────────────────────────────────────────────
# Problem Statement 2: Student Scores
# ───────────────────────────────────────────────────────────────

print("\n\n🔹 Problem 2: Student Subject Analysis")

scores_dict = {
    'English': {'Sam': 60, 'Jackson': 74, 'Ahree': 85},
    'History': {'Gloria': 83, 'Sam': 65, 'Isla': 78, 'Aron': 72, 'Gray': 61},
    'Geography': {'Jackson': 92, 'Gloria': 95, 'Isla': 82, 'Aron': 75, 'Ahree': 76},
    'Mathematics': {'Sam': 99, 'Gloria': 74, 'Jackson': 89, 'Ahree': 85, 'Gray': 95},
    'Science': {'Sam': 89, 'Aron': 82, 'Gray': 78, 'Isla': 93, 'Ahree': 87}
}

# Step 1: Create Series and convert to DataFrame
student_series = pd.Series(scores_dict)
student_df = pd.DataFrame(student_series).T.fillna(0)

# Step 2: Transpose and add average column
transposed_df = student_df.T
transposed_df['Average'] = transposed_df.mean(axis=1)

print("\nStudent Scores DataFrame:\n", transposed_df)

# ───────────────────────────────────────────────────────────────
# Problem Statement 3: Numbers Divisible by 7 and 17
# ───────────────────────────────────────────────────────────────

print("\n\n🔹 Problem 3: Numbers from 1 to 1000 divisible by both 7 and 17")

series_1000 = pd.Series(range(1, 1001))
div_by_7_and_17 = series_1000[(series_1000 % 7 == 0) & (series_1000 % 17 == 0)]
print("Numbers divisible by both 7 and 17:\n", div_by_7_and_17.tolist())

# ───────────────────────────────────────────────────────────────
# Problem Statement 4: Cereal Ratings Visualization
# ───────────────────────────────────────────────────────────────

print("\n\n🔹 Problem 4: Cereal Rating Visualization")

# Step 1: Load cereal dataset
cereal_df = pd.read_csv("https://www.dropbox.com/s/idnul34dfo5cnke/cereal.csv?dl=1")

# Step 2–4: Plot using seaborn style
plt.style.use('seaborn')
plt.figure(figsize=(10, 6))
sns.boxplot(x='MFR', y='rating', data=cereal_df)
plt.title("Cereal Ratings by Manufacturer")
plt.xlabel("Manufacturer")
plt.ylabel("Rating")
plt.ylim(0, 100)
plt.grid(True)
plt.tight_layout()
plt.show()
