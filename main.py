height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#  Convert string to float
h_float = float(height)
w_float = float(weight)

# Calculate BMI weight/height^2
bmi = w_float / h_float ** 2

# Convert to integer
bmi_integer = int(bmi)

# Show integer
print(bmi_integer) 