height = float(input("Your height (in inches): "))
weight = float(input("Your weight (in lbs): "))
bmi = weight * 703 / height ** 2
bmi = round(bmi, 2)

if bmi < 16:
    category = "severly Underweight"
elif bmi < 18.4: 
    category = "underweight"
elif bmi < 24.9: 
    category = "normal"
elif bmi < 29.9: 
    category = "overweight" 
elif bmi < 34.9: 
    category = "Moderately obese"
elif bmi < 34.9: 
    category = "severly obese"
elif bmi > 39.9: 
    category = "morbidly obese"

print(f"Your BMI is {bmi}! It seems you're {category}!")