while True:
    try:
        height = float(input("Enter height in meters: "))
        weight = float(input("Enter weight in kilograms: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if height <= 0 or weight <= 0:
    print("Invalid input. Height and weight must be positive numbers.")
else:
    bmi = weight / (height ** 2)
    bmi_category = ""

    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_category = "Normal weight"
    elif 25 <= bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    print(f"Your BMI is {round(bmi, 2)} which is {bmi_category} according to WHO reference.")
