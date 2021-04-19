pieces = {'wking': 1, 'wqueen':1, 'wbishop': 2, 'wpawn': 8, 'wknight': 4, 'wrook':4, 'bking': 1, 'bqueen':1, 'bbishop': 2, 'bpawn': 8, 'bknight': 4, 'brook':4}
spaces = ['1a', '2b', '3c', '4d', '5e', '6f', '7g', '8h']

def isValidChessBoard(pieces, spaces):
  print('Input piece :')
  piece = str(input())
  print('choose space :')
  space = str(input())
  if piece in pieces and space in spaces:
    print('True')
  else:
    print('False')

isValidChessBoard(pieces, spaces)