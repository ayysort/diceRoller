import random

#   **  DICE BANK   **

def fourdice():
    while True:
        dice = random.randint(1, 4)
        roll = input("Press Enter to roll the dice: ")

        if roll == '':
            print(' ')
            print(' * ', dice, ' *')
            print(' ')
        elif roll == "end":
            break
        else:
            print('Wrong Input')

def sixdice():
    while True:
        dice = random.randint(1, 6)
        roll = input("Press Enter to roll the dice: ")

        if roll == '':
            print(' ')
            print(' * ', dice, ' *')
            print(' ')
        elif roll == "end":
            break
        else:
            print('Wrong Input')

def eightdice():
    while True:
        dice = random.randint(1, 8)
        roll = input("Press Enter to roll the dice: ")

        if roll == '':
            print(' ')
            print(' * ', dice, ' *')
            print(' ')
        elif roll == "end":
            break
        else:
            print('Wrong Input')

def tendice():
    while True:
        dice = random.randint(1, 10)
        roll = input("Press Enter to roll the dice: ")

        if roll == '':
            print(' ')
            print(' * ', dice, ' *')
            print(' ')
        elif roll == "end":
            break
        else:
            print('Wrong Input')
                     
def twelvedice():
    while True:
        dice = random.randint(1, 12)
        roll = input("Press Enter to roll the dice: ")

        if roll == '':
            print(' ')
            print(' * ', dice, ' *')
            print(' ')
        elif roll == "end":
            break
        else:
            print('Wrong Input')

def twentydice():
    while True:
        dice = random.randint(1, 20)
        roll = input("Press Enter to roll the dice: ")

        if roll == '':
            print(' ')
            print(' * ', dice, ' *')
            print(' ')
        elif roll == "end":
            break
        else:
            print('Wrong Input')

#   **  DICE BANK   **


#   **  SELECT SCREEN   **

while True:
    print(' ')
    print(' ')
    print(' ')
    
    print("Please Select a Dice")
    print("   type '0' to leave")
    select = input('(4, 6, 8, 10, 12, 20, 0): ')

    if select == '4':
        print(' ')
        print(' ')
        print(' ')
        print('You are now rolling a FOUR sided dice.')
        print("   Type 'end' to leave.")
        
        fourdice()
    elif select == '6':
        print(' ')
        print(' ')
        print(' ')
        print('You are now rolling a SIX sided dice.')
        print("   Type 'end' to leave.")
        
        sixdice()
    elif select == '8':
        print(' ')
        print(' ')
        print(' ')
        print('You are now rolling an EIGHT sided dice.')
        print("   Type 'end' to leave.")
        
        eightdice()
    elif select == '10':
        print(' ')
        print(' ')
        print(' ')
        print('You are now rolling an TEN sided dice.')
        print("   Type 'end' to leave.")
        
        tendice()
    elif select == '12':
        print(' ')
        print(' ')
        print(' ')
        print('You are now rolling an TWELVE sided dice.')
        print("   Type 'end' to leave.")
        
        twelvedice()
    elif select == '20':
        print(' ')
        print(' ')
        print(' ')
        print('You are now rolling an TWENTY sided dice.')
        print("   Type 'end' to leave.")
        
        twentydice()
    elif select == '0':
        break
    elif select == '':
        print('*** Wrong Input ***')
    else:
        print('*** Wrong Input ***')

#   **  SELECT SCREEN   **

#   **  END   **
print(' ')
print(' ')
print('Have a great day!')
print(' ')
print(' ')





# less efficient
'''
dice = ['1', '2', '3', '4', '5', '6']
print(random.choice(dice))

'''
