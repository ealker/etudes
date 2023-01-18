# Program to read in some text and count the instances of individual words. 

with open('speech.txt', 'r') as file:
  speech = file.read()



speech = open('speech.txt', 'r').read()



print speech.split('\n')



for line in speech:
    lineWords = line.split()


    for word in lineWords:
         print word





#Strip punctuation.
#Lower Case - Group all words together.
#Count function.
