inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


#dict(zip([1,2,3,4], [a,b,c,d]))

def addtoinventory(inventory,lootlist):
    for i in range(len(lootlist)):
        if lootlist[i] in inventory:
            inventory[lootlist[i]] = inventory[lootlist[i]] + 1
        else:
            inventory.setdefault(lootlist[i],1)
    return print(inventory)

addtoinventory(inv, dragonLoot)