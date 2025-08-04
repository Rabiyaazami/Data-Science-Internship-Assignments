from scipy.stats import norm

mean = 75
std_dev = 15
x = float(input("Enter speed X (in km/hr): "))

prob = 1 - norm.cdf(x, loc=mean, scale=std_dev)
print(round(prob, 4))
