import re

upperTest = False
lowerTest = False
digitTest = False
lengthTest = False
password = ''

password = input('Please input your password: ')

print('Evaluating strength...')

upperRegex = re.compile(r'[A-Z]')
moUpper = upperRegex.search(password)
upperTest = not (moUpper == None)

lowerRegex = re.compile(r'[a-z]')
moLower = lowerRegex.search(password)
lowerTest = not (moLower == None)

digitRegex = re.compile(r'\d')
moDigit = digitRegex.search(password)
digitTest = not (moDigit == None)

lengthRegex = re.compile(r'(.*){,7}')
moLength = lengthRegex.search(password)
lengthTest = not (moLength == None)

if(upperTest and lowerTest and digitTest and lengthTest):
    print('Your password is strong enough!')
else:
    print('Your password is weak.')


print('upperTest:' + str(upperTest) + '\nlowerTest:' + str(lowerTest) + '\ndigitTest:' + str(digitTest) + '\nlengthTest:' + str(lengthTest))
