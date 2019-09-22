import os
import re
libString = ''

libsFile = open('./Mad_Libs.txt', 'r')
madLibsFile = libsFile.read()
madLibs = str(madLibsFile)
print(madLibs)

adjectiveRegex = re.compile(r'(ADJECTIVE)') #Adjective case, compile for the word, and search to check later
moAdjective = adjectiveRegex.search(madLibs)
while moAdjective != None:
    libString = input('Please input an Adjective: ')
    madLibs = adjectiveRegex.sub(libString, madLibs)
    moAdjective = adjectiveRegex.search(madLibs)
#print(moVerb)
adverbRegex = re.compile(r'(ADVERB)')#Adverb case
moAdverb = adverbRegex.search(madLibs)
while moAdverb != None:
    libString = input('Please input an Adverb: ')
    madLibs = adverbRegex.sub(libString, madLibs)
    moAdverb = adverbRegex.search(madLibs)
    #print(madLibs)
    #print(moAdverb)
nounRegex = re.compile(r'(NOUN)')#Noun case
moNoun = nounRegex.search(madLibs)
while moNoun != None:
    libString = input('Please input an Noun: ')
    madLibs = nounRegex.sub(libString, madLibs)
    moNoun = nounRegex.search(madLibs)
verbRegex = re.compile(r'(VERB)')#Verb case
moVerb = verbRegex.search(madLibs)
while moVerb != None:
    libString = input('Please input an Verb: ')
    madLibs = verbRegex.sub(libString, madLibs)
    moVerb = verbRegex.search(madLibs)

libsFile = open('./Mad_Libs.txt', 'w')#Overwrite with completed Mad Lib.
libsFile.write(madLibs)
print(madLibs)

clearFile = open('./Mad_Libs.txt', 'w')#reset the file for testing
clearFile.write('The NOUN went and ADVERB VERB the ADJECTIVE')
