import random


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
  


while True:
    print(' ')
    print(' ')
    print(' ')
    
    print("Please Select a Dice")
    print("   type '0' to leave")
    select = input('(6, 8, 0): ')

    if select == '6':
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
    elif select == '0':
        break
    elif select == '':
        print('*** Wrong Input ***')
    else:
        print('*** Wrong Input ***')







# another way
'''
dice = ['1', '2', '3', '4', '5', '6']
print(random.choice(dice))

'''



# NEED TO LOOP
# ADD MULPTIPLE DICE
#   4, 6, 8, 10, 12, 20

