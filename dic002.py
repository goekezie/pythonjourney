player = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
  print("Inventory:")
  item_total = 0
  for k, v in inventory.items():
    item_total =  str(v) + ' ' + k
    print( str(item_total))

  total = 0
  for k, v in inventory.items():
    total = total + v
  print("Total number of items: " + str(total))

displayInventory(player)

