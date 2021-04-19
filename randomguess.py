import random

secretrandom = random.randint(1, 20)
print("i am thinking of number between 1 and 20 ")

for guesstaken in range(1, 7):
  guess = int(input("take a guess: "))
  if guess > secretrandom:
    print("Your guess is too high")
  elif guess < secretrandom:
    print("Your guess is too low")
  else:
    break

if guess == secretrandom:
  print("Congratulations my nigger you guessed correctly after "+ str(guesstaken) + " guesses")
else:
       
  print("You suck my secret number is " + str(secretrandom))
  
