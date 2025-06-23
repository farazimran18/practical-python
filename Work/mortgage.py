# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05  # annual
payment = 2684.11
total_paid = 0.0
num_months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment_val = 1000

while principal > 0:
    num_months += 1
    extra_payment = (
        extra_payment_val
        if (extra_payment_start_month <= num_months <= extra_payment_end_month)
        else 0
    )

    total_payment = payment + extra_payment
    principal = principal * (1 + rate / 12)

    if total_payment > principal:
        total_payment = principal

    principal = principal - total_payment
    total_paid = total_paid + total_payment

    print(
        f"{round(num_months, 2):>5} {round(total_paid, 2):>12} {round(principal, 2):>12}"
    )

print("\nTotal paid", round(total_paid, 2))
print(f"{num_months} months")
