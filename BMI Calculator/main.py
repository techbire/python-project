# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x=float(height)
y=float(weight)
bmi =y / (x ** 2)
print(height,"/","(",weight,"x",weight,")","=", bmi)
z=round(bmi)


if z<18.5:
  print(f"Your BMI is {z}, you are underweight.")
elif z<25:
  print(f"Your BMI is {z}, you have a normal weight.")
elif z<30: 
  print(f"Your BMI is {z}, you are overweight.")
elif z<35:
  print("Your BMI is {z}, you are obese.")
else:
  print("Your BMI is {z}, you are clinically obese.")
