item_count = 0
inventory = {'Object': 12, 'Guns': 23, 'Swords': 2}
dragon_loot = ['Dragun', 'Beholster\'s eye', 'Galanese cannon']


#Defintion of function also goes in the header
def addToInventory(inventory, newItems):
    iteration = 0
    while iteration < len(newItems):
        inventory.setdefault(newItems[iteration], 0)
        iteration = iteration + 1

    iteration = 0
    while iteration < len(newItems):
        inventory[newItems[iteration]] = inventory[newItems[iteration]] + 1
        iteration = iteration + 1

print('Loot found:' + str(dragon_loot))

#Runs the newly defined function
addToInventory(inventory, dragon_loot)

#Code from Fantasy_Inventory.py, still works.
print("Inventory:")

for k, v in inventory.items():
    print(str(v) + ' ' + k)
    item_count = item_count + v

print("Total number of items: " + str(item_count))
