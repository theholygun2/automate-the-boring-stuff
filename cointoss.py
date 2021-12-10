import random
import pprint

numberOfStreaks = 0
coin_list = []
streak_counts = 0

for experimentNumber in range(100):
    rand = random.randint(0,1)
    if not coin_list:
        coin_list += str(rand)
    else:
        if streak_counts == 5:
            numberOfStreaks += 1
            streak_counts = 0

        coin_list += str(rand)
        if coin_list[experimentNumber - 1] == str(rand):
            streak_counts += 1
        else:
            streak_counts = 0


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



#print(f'{experimentNumber} has the value of: {rand}')
    # Code that creates a list of 100 'heads' or 'tails' values.

    # Code that checks if there is a streak of 6 heads or tails in a row.

print('Chance of streak: %s%%' % (numberOfStreaks / 100))


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        print(v)
        numBrought = numBrought + v.get(item, 0)
    return numBrought

#print( 'apples ' + str(totalBrought(allGuests, 'apples')))





horzBoard = ['a','b','c','d','e','f','g','h']
validLoc = []
for i in horzBoard:
    for x in range(1, 9):
        validLoc += [str(x) + i]

#print(validLoc)
#vertBoard = {'1': '','2': '','3': '','4': '','5': '','6': '','7': '','8': ''}
chessBoard1 = {}
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking' ,'2f': 'bpawn','3f': 'bpawn','4f': 'bpawn', '5f': 'bpawn','6f': 'bpawn','7f': 'bpawn','8f': 'bpawn','2c': 'bpawn'}

white = {}
black = {}
chessrules = {'location': validLoc,
                'king': ['bking', 'wking'],
                'pawn': 8,
                'total': 16}

#valid Location
#1 bking and 1 wking
# 16 valued piece at most 8 pawns


def isValidChessBoard(dict_chess):
    valid = True
    dictz = dict_chess
    white = 0
    wpawn = 0
    black = 0
    bpawn = 0


    for locKey, piece in dictz.items():
        print(piece)
        if piece[0] == 'w':
            white += 1
            if piece[1:5] == 'pawn':
                wpawn +=1

        if piece[0] == 'b':
            black += 1
            if piece[1:5] == 'pawn':
                bpawn +=1

        if locKey not in chessrules['location']:
             valid = False

        if chessrules['king'][0] not in dictz.values() and chessrules['king'][1] not in dictz.values():
            valid = False

    if white > 16 or black > 16:
        valid = False

    if wpawn > 8 or bpawn > 8:
        valid = False

    print(white)
    print(black)
    print(wpawn)
    print(bpawn)
    return valid

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    totalItem = 0
    print('invetory: ')
    for key, item in inventory.items():
        print(f'{item} {key}')
        totalItem += item
    print('total number of items ' + str(totalItem))

print(displayInventory(stuff))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']#addedItems
inv = {'gold coin': 42, 'rope': 1}

def addToInventory(inventory, addedItems):
    newDict = inventory
    for item in addedItems:
        newDict.setdefault(item, 0)
        newDict[item] += 1
    return newDict

inv = addToInventory(inv, dragonLoot)
print(displayInventory(inv))
"""MULTILINE COMMENT"""





#print(chessrules['location']) #this is important and different find 'location' with the VALUES of the dict
#print('location' in chessrules) # find 'location' in the KEYS in the chessrules dict
#print(chessrules['king'][0])
#print(chessBoard.values())

#print(isValidChessBoard(chessBoard))
