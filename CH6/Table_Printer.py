width = 0
tracker = 0
lineString = ''
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

x = len(tableData)
#print(x)

iteration = 0
while iteration < x:
    y = len(tableData[iteration])
    iterationAlternate = 0
    #print(iterationAlternate)
    #print(y)
    while iterationAlternate < y:
        #print(str(tableData[iteration][iterationAlternate]) + ' ' + str(len(tableData[iteration][iterationAlternate])))
        if width < len(tableData[iteration][iterationAlternate]):
            width = len(tableData[iteration][iterationAlternate])
        iterationAlternate += 1
    iteration += 1

width += 3
#print(width)

#The program has taken the longest string length, and stored it in width

iteration = 0
while iteration < x:
    y = len(tableData[iteration])
    iterationAlternate = 0
    while iterationAlternate < y:
        #print(tableData[iteration][iterationAlternate])
        tableData[iteration][iterationAlternate] = str(tableData[iteration][iterationAlternate]).rjust(width)
        #print(tableData[iteration][iterationAlternate])
        lineString += tableData[iteration][iterationAlternate]
        tracker += 1
        if tracker == 3:
            print(lineString)
            tracker = 0
            lineString = ''
        iterationAlternate += 1
    iteration += 1
