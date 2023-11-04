# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
digit1 = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e") + name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e")

digit2 = name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e")

love_score = int(str(digit1) + str(digit2))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")