import pyperclip

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

longest = [0,0,0]

for index, items in enumerate(tableData):
    for item in tableData[index]:
        if len(item) > longest[index]:
            longest[index] = len(item)

def printTable():
    colWidths = [0] * len(tableData)
    colWidths = longest
    newlist = []

    for x in range(0,4):
        for y in range(0,3):
            print(tableData[y][x])


    # print(tableData[0][0].rjust(colWidths[0],'.') + tableData[1][0] + tableData[2][0])
    # print(tableData[0][1] + tableData[1][1] +tableData[2][1])
    # print(tableData[0][2]+ tableData[1][2]+ tableData[2][2])
    # print(tableData[0][3]+ tableData[1][3]+ tableData[2][3])



def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
#printPicnic(picnicItems, 12, 5)
#printPicnic(picnicItems, 20, 6)

#print(pyperclip.paste())

printTable()
