import pandas as pd
from sklearn.datasets import load_wine
from scipy.stats import norm
import numpy as np

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# Sample of 50 with random_state=100
sample = df['alcohol'].sample(n=50, random_state=100)

# Z-Critical for 95%
z_critical = norm.ppf(0.975)
mean = sample.mean()
std = sample.std()
margin_error = z_critical * (std / np.sqrt(50))

lower = round(mean - margin_error, 3)
upper = round(mean + margin_error, 3)

print("Z-Critical:", round(z_critical, 3))
print("Margin of Error:", round(margin_error, 3))
print("Confidence Interval:", (lower, upper))
