import re


#from collections import Counter

#words = "apple banana apple strawberry banana lemon"

#d = defaultdict(int)
#for word in words.split():
    #d[word] += 1

   #print str(word )+ " " +  str(d[word])


#if (word.length > 0 && word[0] >='A')
            #if len(word)>0 and word[0]>'z' and word[0]<'A':

from collections import Counter



with open('speech.txt', 'r') as file:
    speech = file.readlines()

    for line in speech:
        lineWords = line.split()

        #words = lineWords
        freqCounter = Counter(lineWords)
        print(freqCounter)

        #for word in lineWords:

                print word






