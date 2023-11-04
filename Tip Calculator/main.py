# #If the bill was $150.00, split between 5 people, with 12% tip. 

# #Each person should pay (150.00 / 5) * 1.12 = 33.6
# #Format the result to 2 decimal places = 33.60

# #Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# #Write your code below this line 👇

# # Get user input for bill amount, number of people, and tip percentage
# bill_amount = float(input("Enter the bill amount: ₹"))
# num_people = int(input("Enter the number of people: "))
# tip_percentage = float(input("Enter the tip percentage: "))

# # Calculate the total amount including tip
# total_amount = bill_amount * (1 + tip_percentage / 100)

# # Calculate the amount each person should pay
# amount_per_person = total_amount / num_people

# # Format the result to two decimal places
# formatted_amount = "{:.2f}".format(amount_per_person)

# # Print the result
# print("Each person should pay ₹" + formatted_amount)
from plyer import notification
import time

def set_reminder(title, message, delay_seconds):
    notification.notify(
        title=title,
        message=message,
        app_name='Reminder App',
        timeout=10
    )
    time.sleep(delay_seconds)

if __name__ == "__main__":
    while True:
        title = input("Enter the reminder title: ")
        message = input("Enter the reminder message: ")
        delay_minutes = int(input("Enter the delay in minutes: "))

        delay_seconds = delay_minutes * 60

        set_reminder(title, message, delay_seconds)
