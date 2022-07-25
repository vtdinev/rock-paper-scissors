import random

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

user_choise = int(input("Please enter 0, 1 or 2 "))
cpu_choise = random.randint(0, 2)
if user_choise < 0 or user_choise > 2:
    print("Enter a valid number")
else:
    if user_choise == 0:
        draw_user_choise = rock
        print(draw_user_choise)
        if cpu_choise == 0:
            draw_cpu_choise = rock
            print(draw_cpu_choise)
            print("draw")
        elif cpu_choise == 1:
            draw_cpu_choise = paper
            print(draw_cpu_choise)
            print("You Lose")
        else:
            draw_cpu_choise = scissors
            print(scissors)
            print("You Win")
    elif user_choise == 1:
        draw_user_choise = paper
        print(draw_user_choise)
        if cpu_choise == 1:
            draw_cpu_choise = paper
            print(draw_cpu_choise)
            print("draw")
        elif cpu_choise == 0:
            draw_cpu_choise = rock
            print(draw_cpu_choise)
            print("You Win")
        else:
            draw_cpu_choise = scissors
            print(scissors)
            print("You Lose")
    elif user_choise == 2:
        draw_user_choise = scissors
        print(draw_user_choise)
        if cpu_choise == 0:
            draw_cpu_choise = rock
            print(draw_cpu_choise)
            print("You Lose")
        elif cpu_choise == 1:
            draw_cpu_choise = paper
            print(draw_cpu_choise)
            print("You Win")
        else:
            draw_cpu_choise = scissors
            print(scissors)
            print("Draw")
