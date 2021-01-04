# Yingcan Chen CSC191 Assignment 5
# 2020 oct-4
import random as r

# Problem 5.1
myList=["Urus", "miata", "Mustang", "Challenger", "911GT3RS", "Huracan", "488Pista"]
myListNameSingular = "Performance Car"
myListNamePlural = "Performance Cars"
print("Problem 5.1")
print("-----------")
print("My collection contains {}".format(myListNamePlural))
print()

# Problem 5.2
numItems = len(myList)
print("Problem 5.2")
print("-----------")
print("My collection contains {} {} items".format(numItems, myListNameSingular))
print()

# Problem 5.3
print("Problem 5.3")
print("-----------")
for car in myList:
    print(car)
print()

# Problem 5.4
print("Problem 5.4")
print("-----------")
counter = 0
while (counter <= numItems-1):
    print("\t {}. {}".format(counter+1, myList[counter]))
    counter += 1
print()

# Problem 5.5 Part A, B, C and D
firstItemToBeRemoved = "miata"
secondItemToBeRemoved = "Huracan"
myList.remove(firstItemToBeRemoved)
myList.remove(secondItemToBeRemoved)
print("Problem 5.5")
print("-----------")
print("The first {} removed was '{}'.".format(myListNameSingular, firstItemToBeRemoved))
print("The second {} removed was '{}'.".format(myListNameSingular, secondItemToBeRemoved))
itemToBeInserted = "McLaren GT"
myList.insert(1, itemToBeInserted)
print("The {} inserted was '{}'.".format(myListNameSingular, itemToBeInserted))
numItems = len(myList)
itemPopped = myList.pop(numItems-1)
print("The {} popped off was '{}'.".format(myListNameSingular, itemPopped))
print()
for car in myList: 
    print(car)
print()

# Problem 5.6
lottoNumbers = []
for i in range(5):
    lottoNumber = r.randint(1, 70)
    lottoNumbers.append(lottoNumber)
megaBallNumber = r.randrange(1, 26)
lottoOutput = ""
counter = 0
while (counter != -1):
    lottoNumber = lottoNumbers[counter]
    lottoOutput = lottoOutput + str(lottoNumber) + " "
    if counter >= len(lottoNumbers)-1:
        break
    counter += 1
lottoOutput = lottoOutput + "Mega Ball: " + str(megaBallNumber)
print("Problem 5.6")
print("-----------")
print("My Python Lottery Ticket:\n\n{}".format(lottoOutput))
print()

# Problem 5.7
numTickets = r.randint(1, 10)
print("Problem 5.7")
print("-----------")
print("My {} Python Lottery Tickets:".format(numTickets))
print()
for i in range(numTickets):
    lottoNumbers = []
    for i in range(5):
        lottoNumber = r.randint(1, 70)
        lottoNumbers.append(lottoNumber)
    megaBallNumber = r.randrange(1, 26)
    lottoOutput = ""
    counter = 0
    while counter != -1:
        lottoNumber = lottoNumbers[counter]
        if lottoNumber < 10:
            lottoOutput = lottoOutput + "0" + str(lottoNumber) + " "
        else:
            lottoOutput = lottoOutput + str(lottoNumber) + " "
        if counter >= len(lottoNumbers)-1:
            break
        counter += 1
    if megaBallNumber < 10:
        lottoOutput = lottoOutput + "Mega Ball: " + "0" + str(megaBallNumber)
    else:
        lottoOutput = lottoOutput + "Mega Ball: " + str(megaBallNumber)
    print(lottoOutput)