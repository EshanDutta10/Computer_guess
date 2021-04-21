import random

def computer_guess(num):
    low = 1
    high = num
    feedback = ''
    while feedback != 'c' and low != high:
        g = random.randint(low, high)
        feedback = input(f"Is {g} too high (H), too low (L) or Correct (C)? ").lower()
        if feedback == 'h':
            high = g - 1
        elif feedback == 'l':
            low = g + 1

    print(f"The computer Guessed your number {g} correctly!")

computer_guess(50)

