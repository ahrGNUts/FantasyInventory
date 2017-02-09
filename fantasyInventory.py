from random import randint

theInventory = {'shirt': 1, 'breeches': 1, 'shortsword': 1,
                'potion': 1, 'apple': 1, 'gold': 14}

loot = ('armor', 'gold', 'potion', 'apple', 'gold', 'longsword', 'diamond', 'talisman')

choice = 1


def displayPrompt():
    print('Hail adventurer! What is your next move?')
    print('1. Display inventory')
    print('2. Search the nearby area for items')
    print('3. Quit game')

    return int(input())


def displayInventory(inventory):
    for key, val in inventory.items():
        print(key, ":", val)


def addRandomItem(inventory):
    # adds a random item to player inventory
    print('Now searching nearby area.')
    for i in range(5):
        print('.' * i)

    foundItem = randint(0, 1)

    if foundItem == 1:
        itemType = randint(0, len(loot) - 1)
        if itemType == 1:
            # if you find gold, you get more than one gold, other things you usually get 1-2 items
            itemAmount = randint(3, 45)
        else:
            itemAmount = 1

        print('Found ' + str(itemAmount) + ' ' + loot[itemType] + '!')
        print('Stowing in your sack...')

        if loot[itemType] in inventory:
            theInventory[loot[itemType]] += itemAmount
        else:
            theInventory[loot[itemType]] = itemAmount
    else:
        print("Couldn't find anything!")

while True:
    choice = displayPrompt()

    if choice == 1:
        displayInventory(theInventory)
    elif choice == 2:
        addRandomItem(theInventory)
    elif choice == 3:
        print('Peace be with you traveler!')
        break