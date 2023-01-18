

with open('speech.txt', 'r') as file:
    speech = file.readlines()

    for line in speech:
        lineWords = line.split()

         print lineWords

