#Blow are the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choose= int(input("choose 1 for rock,2 for paper, 3 for scissors"))
computer_chose=int(random.randint(1,3))
if choose==1:
    print(rock)
    print("you chose ROCK(1)")
elif choose==2:
    print(paper)
    print("you chose PAPER(2)")
else:
    print(scissors)
    print("you chose SCISSORS(3)")


print(computer_chose)
if computer_chose==1:
    print(rock)
    print("Computer chose ROCK")
elif computer_chose==2:
    print(paper)
    print("computer chose PAPER")
else:
    print(scissors)
    print("computer chose SCISSORS")




if choose > computer_chose:
    print("YOU WON")
elif choose< computer_chose:
    print("Computer won")
else:
    print("DRAW-PLEASE PLAY AGAIN")

 
