bill_thickness = 0.11 * 0.001  # meters (0.11 mm)
sears_height = 442  # meters
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    day += 1
    num_bills *= 2

print(f"{day} days")
print(f"{num_bills} bills")
print(f"{bill_thickness * num_bills} meters")
