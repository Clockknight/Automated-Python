sampleList = ['Quantum Thing 0', 'Thing One', 'Thing Two']
endString = ''
i = 0

print('Beginning convertion of sampleList.')
sampleLength = len(sampleList)


while True:
    if (sampleLength - i) == sampleLength:
        endString = endString + sampleList[i]
    elif (sampleLength - i) == 1:
        endString = endString + ', and' + sampleList[i]
    else:
        endString = endString + ', ' + sampleList[i]
    i = i + 1
    if (sampleLength == i):
        break

print(endString)
