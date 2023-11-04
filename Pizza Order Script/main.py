# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0 
if size == "S":
    bill += 100
elif size == "M":
    bill += 150
elif size == "L":
    bill += 200

if add_pepperoni == "Y":
  if size == "S":
    bill += 40
  elif size == "M":
    bill += 70
  elif size == "L":
    bill += 100

if extra_cheese == "Y":
  bill += 25
else:
  bill +=0

print(f"Your final bill is ₹{bill}")