import os
import sys
import time
import pyinputplus as pyip

i = 0
score = 0

while i < 10:
    iStr = str(i)
    iSq = i * i
    print('Please solve the following multiplication equation in eight seconds:\n' + iStr + ' x ' + iStr)

    try:
        answer = pyip.inputInt('\n\nYour answer?: ', min=iSq, max=iSq, limit=3, timeout=8)

    except pyip.TimeoutException:
        print("Time up! Question marked incorrect.")

    except pyip.RetryLimitException:
        print("Too many tries. Question marked incorrect.")

    else:
        score += 1
        time.sleep(1)

    i += 1

print('TOTAL SCORE: ' + str(score) + '/10. Good effort!')
