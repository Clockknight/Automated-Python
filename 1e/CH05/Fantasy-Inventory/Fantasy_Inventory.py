inventory = {'object': 12, 'guns': 23, 'swords': 2}
item_count = 0

print("Inventory:")

for k, v in inventory.items():
    print(str(v) + ' ' + k)
    item_count = item_count + v

print("Total number of items: " + str(item_count))
