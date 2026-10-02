import statistics

# Given dataset
data = [10, 20, 20, 30, 40, 50, 50, 60, 70, 80]

print("Dataset:")
print(data)

# Mean
mean = statistics.mean(data)
print("\nMean:", mean)

# Median
median = statistics.median(data)
print("Median:", median)

# Mode
mode = statistics.mode(data)
print("Mode:", mode)

# Variance
variance = statistics.variance(data)
print("Variance:", variance)

# Standard Deviation
std_dev = statistics.stdev(data)
print("Standard Deviation:", std_dev)

# Range
data_range = max(data) - min(data)
print("Range:", data_range)

# Quartiles
sorted_data = sorted(data)

q1 = statistics.quantiles(data, n=4)[0]
q2 = statistics.quantiles(data, n=4)[1]
q3 = statistics.quantiles(data, n=4)[2]

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)

# Interquartile Range
iqr = q3 - q1
print("IQR:", iqr)