# Yingcan Chen
# Sept/24/2020
# CIS191 Assignment4
# Part1
print("Welcome to Python Airlines!")

# Part2
firstName = input("What is your first name?")

miles = input("How many miles have you flown?")

segments = input("How many segments have you flown?")

DollarsSpent = input("How much money have you spent (USD)?")

# Part3
miles = int(miles)

segments = int(segments)

DollarsSpent = float(DollarsSpent)

# Part4
Tier = ""
if miles >= 100000 and segments > 120 and DollarsSpent >= 15000.00:
    Tier = "Diamond"
elif miles >= 75000 and segments > 90 and DollarsSpent >= 9000.00:
    Tier = "Ruby"
elif miles >= 50000 and segments > 60 and DollarsSpent >= 6000.00:
    Tier = "Emerald"
elif miles >= 25000 and segments > 30 and DollarsSpent >= 3000.00:
    Tier = "Sapphire"
else:
    Tier = "None"

# Part5-Determine the Rewards
# Initialize Rewards variables
FreeBags = 0
FreeSeat = ""
FreeAccess = False
if Tier == "Diamond":
    FreeBags = 3
    FreeSeat = "First"
    FreeAccess = True
elif Tier == "Ruby":
    FreeBags = 2
    FreeSeat = "First"
elif Tier == "Emerald":
    FreeBags = 1
    FreeSeat = "Business"
elif Tier == "Sapphire":
    FreeBags = 0
    FreeSeat = "Business"
else:
    FreeBags = 0
    FreeSeat = "None"
    FreeAccess = False

# Part6-Display an input Summary
print("You have flown {} flights for {:,} miles and spent ${:,.2f} USD with Python Airlines.".format(segments, miles, DollarsSpent))

# part7- Display the Membership Tier
if Tier != "None":
    print("{}, you have achieved {}-level frequent-flier status with Python Airlines!".format(firstName,Tier))
else:
    print("{}, we're sorry, you have not yet achieved frequent-flier status with Python Airlines.".format(firstName))

# part8-Display the Reward Summary

if Tier != "None":
    print("You have unlocked the following rewards:")
    if FreeBags:
        print("- {} free checked bags per flight".format(FreeBags))
    print("- Free seat upgrades to {} Class".format(FreeSeat))
    if FreeAccess == True:
        print("- Free access to the club lounge")






