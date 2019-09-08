width = 0
iteration = 0
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

while iteration < len(tableData):
    if len(tableData[iteration]) > width:
        width = len(tableData[iteration])
    iteration += 1

width += 3

print(width)
