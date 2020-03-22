import time
import pyperclip

#Display the progrm's instructions,
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1
lapStringList = ''

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        lapTimeString = str(lapTime)
        totalTimeString = str(totalTime)
        lapNumString = str(lapNum)

        lapString = 'Lap #' + lapNumString.rjust(3) + ': ' + totalTimeString.rjust(7) + ' (' + lapTimeString.rjust(6) + ')'
        lapStringList += lapString + '\n'

        print(lapString, end='')

        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone.')
    pyperclip.copy(lapStringList)
