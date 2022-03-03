# Problem: Write a bit of code that will take in a number n, and have it print the multiplication table from 1 to n.

limit = int(input("Enter a number: ")) 


def calculate_table(multiplicand):
    table = []
    for i in range(1, limit+1):
        table.append(multiplicand * i)
    print(table)

for j in range(1, limit+1):
    calculate_table(j)
