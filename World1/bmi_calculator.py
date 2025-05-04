''' Develop a logic that reads a person's weight and height, calcule their BMI and displays their status, 
according to the table below:
- Below 18.5: Underweight
- Between 18.5 and 25: Ideal weight
- 25 to 30: Overweight
- 30 to 40: Obesity
- Over 40: Morbidly obese '''

weight = float(input("Enter the person's weight: "))
height = float(input("Enter the person's height: "))

if weight <= 0 or height <= 0:
    print("\nError: Weight and height must be positive values.")
    exit()

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"BMI: {bmi:.2f} \nThe person is Underweight.")
elif bmi < 25:
    print(f"BMI: {bmi:.2f} \nThe person is Ideal Weight.")
elif bmi < 30:
    print(f"BMI: {bmi:.2f} \nThe person is Overweight.")
elif bmi < 40:
    print(f"BMI: {bmi:.2f} \nThe person is Obesity.")
else:
    print(f"BMI: {bmi:.2f} \nThe person is Morbidly Obese.")