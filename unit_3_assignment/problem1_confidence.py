from scipy.stats import norm

n = 200
x = int(input("Enter number of highly satisfied customers: "))
p_hat = x / n
z_critical = norm.ppf(0.95)
std_error = (p_hat * (1 - p_hat) / n) ** 0.5
margin_of_error = z_critical * std_error

lower = round(p_hat - margin_of_error, 5)
upper = round(p_hat + margin_of_error, 5)
print(lower, upper)
5