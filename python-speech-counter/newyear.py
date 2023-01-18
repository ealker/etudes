__author__ = 'Elliot Alker'

#Cooper's generic New Year's speech.

print "Enter the fields to complete this generic New Year's speech!"

year = input("Enter previous year: ")
adjective1 = raw_input("Type in an adjective: ")
event1 = raw_input("Enter an event name: ")
event2 = raw_input("Enter another event name: ")
adjective2 = raw_input("Type in a second adjective: ")
adjective3 = raw_input("Type in a third adjective: ")
name1 = raw_input("Enter a friend's name: ")
name2 = raw_input("Enter another friend's name (if you have more than one friend): ")
name3 = raw_input("Enter a third friend's name: ")
adjective4 = raw_input("Enter a final adjective: ")
newyear = year + 1

print "Wow,",year, "was an", adjective1, "year!"
print "Do you remember the", event1 , "or the", event2 ,"?"
print "What an" , adjective2 , "year, but next year will be even more" , adjective3 ,"."
print "I'd like to thank", name1 ,",", name2 , "and", name3 , "for making this year extra",adjective4 ,"."
print "See you in", newyear,"!!!"