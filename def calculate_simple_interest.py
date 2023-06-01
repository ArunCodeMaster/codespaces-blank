def calculate_simple_interest(principal, time, gender, senior_citizen):
    if gender.lower() == 'female':
        if senior_citizen:
            rate = 8
        else:
            rate = 6
    else:
        if senior_citizen:
            rate = 7
        else:
            rate = 5

    interest = (principal * rate * time) / 100
    return interest


# Example usage
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period (in years): "))
gender = input("Enter the customer's gender (Male/Female): ")
senior_citizen = input("Is the customer a senior citizen? (yes/no): ")

if senior_citizen.lower() == 'yes':
    senior_citizen = True
else:
    senior_citizen = False

interest = calculate_simple_interest(principal, time, gender, senior_citizen)
total_amount = principal + interest

print("Simple Interest: ", interest)
print("Total Amount: ", total_amount)
