# Program to read in some text and count the instances of individual words. 
from collections import Counter
import re

words = re.findall(r'\w+', open('speech.txt').read().lower())
# words = re.split('\d+', open('speech.txt').read().lower())
for key, value in Counter(words).most_common():
    print(key, value)