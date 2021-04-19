import random, sys

#varibles
wins = 0
losses = 0
ties = 0

while True: #main game loop
  print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
  while True: #player input Loop 
    print("Enter Your move: (r)ock (p)aper (s)cissors or (q)uit")
    PlayerMove = input()
    if PlayerMove == 'q':
      sys.exit()
    if PlayerMove == 'r' or PlayerMove == 'p' or PlayerMove == 's':
      break
    print('type one: r, p, s or q')

  if PlayerMove == 'r':
    print('Rock versus ...')
  elif PlayerMove == 'p':
    print('Paper versus ...')
  elif PlayerMove == 's':
    print('Scissors versus ...')

  #display what computer chooses
  randomnum = random.randint(1, 3)
  if randomnum == 1:
    computermove = 'r'
    print('Rock')
  elif randomnum == 2:
    computermove = 'p'
    print('Paper')  
  elif randomnum == 3:
    computermove = 's'
    print('Scissors')

  #scores
  if PlayerMove == computermove:
    print('Its a tie!')
    ties += 1
  elif PlayerMove == 'r' and computermove == 's':
    print('You win!')
    wins += 1
  elif PlayerMove == 'p' and computermove == 'r':
    print('You win!')
    wins += 1
  elif PlayerMove == 's' and computermove == 'p':
    print('You win!')
    wins += 1
  elif PlayerMove == 'r' and computermove == 'p':
    print('You Lose!')
    losses += 1
  elif PlayerMove == 'p' and computermove == 's':
    print('You Lose!')
    losses += 1
  elif PlayerMove == 's' and computermove == 'r':
    print('You Lose!')
    losses += 1