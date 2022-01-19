#increment counter
i = 0

#character class
class Character:
    #attributes for character
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def roster(self):
        print(self.name + " , " + self.age)

#party is a list of Characters
party = []

#partySize is user-defined size of character party list
partySize = 0
partySize = int(input("How many characters are in your party? "))

#party input
while i < partySize:
    currentName = input("What is this character's name? ")
    currentAge = input("What is this character's age? ")
    print("\n")
    #add currentName and currentAge to current character assignment in the loop
    party.append(Character(currentName, currentAge))
    i = i + 1

for Character in party:
    Character.roster()

print("End of test")
input()