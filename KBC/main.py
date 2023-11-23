from art import logo
import random
import pygame
import time
print(logo)

pygame.mixer.init()
pygame.mixer.music.load('kbc.mp3') 
pygame.mixer.music.play()

correct_sound = pygame.mixer.Sound('correctans.mp3')

questions = [
   [
    "Who among the following considered as the 'father of artificial intelligence'?", "Charles Babbage", "Lee De Forest", "John McCarthy","JP Eckert", 3
  ],
  [
    "What is the purpose of the 'grep' command in Unix/Linux?", "To search for a pattern in a file", "To copy files", "To remove files", "To display disk space usage", 1
  ],
  [
    "Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn", 1
  ],
  [
    "In computer science, what does 'SQL' stand for?", "Simple Query Language", "Structured Question Language", "System Query Language", "Structured Query Language", 4
  ],
  [
    "Who directed the movie 'Avengers: Endgame'?", "Christopher Nolan", "William Shakespeare", "Joss Whedon", "Russo Brothers", 4
  ],
  [
   "Which programming language was developed by Guido van Rossum?", "Java", "Python", "C++", "Ruby", 2
  ],
  [
    "Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen", 2
  ],
  [
    "Which element has the chemical symbol 'H'?", "Helium", "Hydrogen", "Lithium", "Nitrogen", 2
  ],
  [
    "Which data structure is typically used for implementing a queue?", "Array", "Linked List", "Stack", "Tree", 2
  ],
  [
    "What is the smallest prime number?", "1", "2", "3", "0", 2
  ],
  [
    "Which famous scientist developed the theory of general relativity?", "Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei",2
  ],
  [
    "Who is the author of the science fiction novel 'Dune'?", "Isaac Asimov", "Philip K. Dick", "Arthur C. Clarke", "Frank Herbert",4
  ],
  [
    "Who painted the Mona Lisa?", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet", 3
  ],
  [
    "What is the time complexity of the quicksort algorithm in the average case?", "O(n)", "O(n log n)","O(n^2)", "O(log n)", 2
  ],
  [
    "What is the name of Luke Skywalker's home planet?", "Lusitania", "Queen Mary", "Tatooine", "Andrea Doria", 3
  ]
]

random.shuffle(questions)

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 10000000]
money = 0
print("\nSwagat hai aapka, kaun banega Crorepati mein !")
for i in range(0, len(questions)):
  
  question = questions[i]
  time.sleep(3)
  print(f"\n\nYeh raha Rs. {levels[i]} ka sawaal aapke computer screen pe:\n")

  print(question[0])
  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  reply = int(input("\nApna jawab dein (1-4) ya 0 dabayein toh bahar jayein is khel se!!:\t"))

  # Correct answer and checkpoint 
  if reply == question[-1]:

    correct_sound.play()

    if i == 14:
      print("\n*********** 1 CRORE *********** ")
      break
    if i == 4 or i == 9:
      money = levels[i]
      print(f"\n Ekdam zabardast! Aapne checkpoint ko paar kiya hai aur bina kisi shak ke, aap ghar lekar jaayenge, Rupees {levels[i]} ke saath ")
    else:
      print(f"\nSahi jawab! Aapne jeet haasil ki hai, Rs. {levels[i]}")

      money = levels[i]

  # quit by contestant 
  if reply == 0:
    break
  # wrong answer by contestant 
  if reply != question[-1]:
   
    

    
    print(f"\nGalat jawab! \nSahi jawab hai: {question[-1]} \nYe antim prashna tha aur aapne bahut achha koshish kiya, \nDhanyavaad aur phir milenge!")

   


    if 0 <= i < 4:
      money = 0
      break
    if 4 <= i < 9:
      money = 10000
      break
    if 9 < i < 14:
      money = 320000
      break

print(f"\nAapne jeet haasil ki hai, Rs.{money}! \nIss khel mein mera saath dene ke liye aapka shukriya, Dhanyavaad!")