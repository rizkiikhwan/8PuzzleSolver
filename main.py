import copy

start = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

end = [[0, 6, 4],
       [1, 3, 8],
       [7, 5, 2]]

round2 = [[2, 3, 4],
          [1, 0, 5],
          [6, 8, 7]]

tester = [[1, 3, 5],
          [2, 8, 4],
          [6, 0, 7]]


totalLooping = 5
totalSimilar = 0
totalBackward = 0

mix = copy.deepcopy([tester])
parent = copy.deepcopy([round2])
currentList = copy.deepcopy(start)

for loops in range(0, totalLooping):

    for checking in range(0, len(mix)):
        if currentList == mix[checking]:
            totalSimilar += 1

    for checkingParent in range(0, len(parent)):
        if currentList == parent[checkingParent]:
            totalBackward += 1

    if totalSimilar < 2:

        # First Row
        if currentList[0][0] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[0][0], swapPosition1[0][1] = swapPosition1[0][1], swapPosition1[0][0]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[0][0], swapPosition2[1][0] = swapPosition2[1][0], swapPosition2[0][0]

            mix.append(swapPosition1)
            mix.append(swapPosition2)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        elif currentList[0][1] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[0][1], swapPosition1[0][2] = swapPosition1[0][2], swapPosition1[0][1]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[0][1], swapPosition2[1][1] = swapPosition2[1][1], swapPosition2[0][1]

            swapPosition3 = copy.deepcopy(currentList)
            swapPosition3[0][1], swapPosition3[0][0] = swapPosition3[0][0], swapPosition3[0][1]

            mix.append(swapPosition1)
            mix.append(swapPosition2)
            mix.append(swapPosition3)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        elif currentList[0][2] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[0][2], swapPosition1[0][1] = swapPosition1[0][1], swapPosition1[0][2]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[0][2], swapPosition2[1][2] = swapPosition2[1][2], swapPosition2[0][2]

            mix.append(swapPosition1)
            mix.append(swapPosition2)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        # Second Row
        elif currentList[1][0] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[1][0], swapPosition1[1][1] = swapPosition1[1][1], swapPosition1[1][0]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[1][0], swapPosition2[0][0] = swapPosition2[0][0], swapPosition2[1][0]

            swapPosition3 = copy.deepcopy(currentList)
            swapPosition3[1][0], swapPosition3[2][0] = swapPosition3[2][0], swapPosition3[1][0]

            mix.append(swapPosition1)
            mix.append(swapPosition2)
            mix.append(swapPosition3)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        elif currentList[1][1] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[1][1], swapPosition1[1][2] = swapPosition1[1][2], swapPosition1[1][1]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[1][1], swapPosition2[1][0] = swapPosition2[1][0], swapPosition2[1][1]

            swapPosition3 = copy.deepcopy(currentList)
            swapPosition3[1][1], swapPosition3[0][1] = swapPosition3[0][1], swapPosition3[1][1]

            swapPosition4 = copy.deepcopy(currentList)
            swapPosition4[1][1], swapPosition4[2][1] = swapPosition4[2][1], swapPosition4[1][1]

            mix.append(swapPosition1)
            mix.append(swapPosition2)
            mix.append(swapPosition3)
            mix.append(swapPosition4)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        elif currentList[1][2] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[1][2], swapPosition1[1][1] = swapPosition1[1][1], swapPosition1[1][2]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[1][2], swapPosition2[0][2] = swapPosition2[0][2], swapPosition2[1][2]

            swapPosition3 = copy.deepcopy(currentList)
            swapPosition3[1][2], swapPosition3[2][2] = swapPosition3[2][2], swapPosition3[1][2]

            mix.append(swapPosition1)
            mix.append(swapPosition2)
            mix.append(swapPosition3)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        # Three Row
        elif currentList[2][0] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[2][0], swapPosition1[2][1] = swapPosition1[2][1], swapPosition1[2][0]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[2][0], swapPosition2[1][0] = swapPosition2[1][0], swapPosition2[2][0]

            mix.append(swapPosition1)
            mix.append(swapPosition2)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        elif currentList[2][1] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[2][1], swapPosition1[1][1] = swapPosition1[1][1], swapPosition1[2][1]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[2][1], swapPosition2[2][2] = swapPosition2[2][2], swapPosition2[2][1]

            swapPosition3 = copy.deepcopy(currentList)
            swapPosition3[2][1], swapPosition3[2][0] = swapPosition3[2][0], swapPosition3[2][1]

            mix.append(swapPosition1)
            mix.append(swapPosition2)
            mix.append(swapPosition3)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        elif currentList[2][2] == 0:
            swapPosition1 = copy.deepcopy(currentList)
            swapPosition1[2][2], swapPosition1[2][1] = swapPosition1[2][1], swapPosition1[2][2]

            swapPosition2 = copy.deepcopy(currentList)
            swapPosition2[2][2], swapPosition2[1][2] = swapPosition2[1][2], swapPosition2[2][2]

            mix.append(swapPosition1)
            mix.append(swapPosition2)

            parent.append(currentList)

            currentList = copy.deepcopy(swapPosition1)

        # In case all of that not happening
        else:
            print("some error in per-number")

    # Pemutaran pertama akan sia - sia, bila nilai current di taruh di akhir.
    elif totalSimilar >= 2:
        totalBackward += 1
        currentList = copy.deepcopy(mix[-totalBackward])
        totalSimilar = 0
        totalBackward = 0

    else:
        print("some error occurrence")

    # Keep this in end first loop
    if loops == 0:
        mix.remove(mix[0])
        mix.insert(0, start)
        parent.remove(parent[0])
        # parent.insert(0, start)

    print("list number:", loops + 1)
    print(currentList, "\n")

print("value of all matrix")
print(mix)
