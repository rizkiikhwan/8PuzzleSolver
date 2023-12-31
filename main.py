import copy

# Start point of 8 puzzle
start = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

# End point of 8 puzzle
end = [[1, 2, 0],
       [3, 4, 5],
       [6, 7, 8]]

testPointParent = [[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]

testPointMix = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]

# Chose how many loops you want
totalLooping = 8

totalSimilar = 0
totalBackward = 0

mix = copy.deepcopy([testPointMix])
parent = copy.deepcopy([testPointParent])
currentList = copy.deepcopy(start)

for loops in range(0, totalLooping):

    if currentList != end:

        for checking in range(0, len(mix)):
            if currentList == mix[checking]:
                totalSimilar += 1

        for checkingParent in range(0, len(parent)):
            if currentList == parent[checkingParent]:
                totalBackward += 1

        print("list number:", loops + 1)
        print(currentList, "\n")

        if totalSimilar < 2:

            totalBackward = 0

            # First Row
            if currentList[0][0] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[0][0], swapPosition1[1][0] = swapPosition1[1][0], swapPosition1[0][0]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[0][0], swapPosition2[0][1] = swapPosition2[0][1], swapPosition2[0][0]

                mix.append(swapPosition1)
                mix.append(swapPosition2)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition2)

            elif currentList[0][1] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[0][1], swapPosition1[0][0] = swapPosition1[0][0], swapPosition1[0][1]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[0][1], swapPosition2[1][1] = swapPosition2[1][1], swapPosition2[0][1]

                swapPosition3 = copy.deepcopy(currentList)
                swapPosition3[0][1], swapPosition3[0][2] = swapPosition3[0][2], swapPosition3[0][1]

                mix.append(swapPosition1)
                mix.append(swapPosition2)
                mix.append(swapPosition3)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition3)

            elif currentList[0][2] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[0][2], swapPosition1[0][1] = swapPosition1[0][1], swapPosition1[0][2]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[0][2], swapPosition2[1][2] = swapPosition2[1][2], swapPosition2[0][2]

                mix.append(swapPosition1)
                mix.append(swapPosition2)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition2)

            # Second Row
            elif currentList[1][0] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[1][0], swapPosition1[2][0] = swapPosition1[2][0], swapPosition1[1][0]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[1][0], swapPosition2[1][1] = swapPosition2[1][1], swapPosition2[1][0]

                swapPosition3 = copy.deepcopy(currentList)
                swapPosition3[1][0], swapPosition3[0][1] = swapPosition3[0][1], swapPosition3[1][0]

                mix.append(swapPosition1)
                mix.append(swapPosition2)
                mix.append(swapPosition3)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition3)

            elif currentList[1][1] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[1][1], swapPosition1[1][0] = swapPosition1[1][0], swapPosition1[1][1]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[1][1], swapPosition2[2][1] = swapPosition2[2][1], swapPosition2[1][1]

                swapPosition3 = copy.deepcopy(currentList)
                swapPosition3[1][1], swapPosition3[1][2] = swapPosition3[1][2], swapPosition3[1][1]

                swapPosition4 = copy.deepcopy(currentList)
                swapPosition4[1][1], swapPosition4[0][1] = swapPosition4[0][1], swapPosition4[1][1]

                mix.append(swapPosition1)
                mix.append(swapPosition2)
                mix.append(swapPosition3)
                mix.append(swapPosition4)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition4)

            elif currentList[1][2] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[1][2], swapPosition1[1][1] = swapPosition1[1][1], swapPosition1[1][2]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[1][2], swapPosition2[2][2] = swapPosition2[2][2], swapPosition2[1][2]

                swapPosition3 = copy.deepcopy(currentList)
                swapPosition3[1][2], swapPosition3[0][2] = swapPosition3[0][2], swapPosition3[1][2]

                mix.append(swapPosition1)
                mix.append(swapPosition2)
                mix.append(swapPosition3)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition3)

            # Three Row
            elif currentList[2][0] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[2][0], swapPosition1[2][1] = swapPosition1[2][1], swapPosition1[2][0]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[2][0], swapPosition2[1][0] = swapPosition2[1][0], swapPosition2[2][0]

                mix.append(swapPosition1)
                mix.append(swapPosition2)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition2)

            elif currentList[2][1] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[2][1], swapPosition1[2][0] = swapPosition1[2][0], swapPosition1[2][1]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[2][1], swapPosition2[2][2] = swapPosition2[2][2], swapPosition2[2][1]

                swapPosition3 = copy.deepcopy(currentList)
                swapPosition3[2][1], swapPosition3[1][1] = swapPosition3[1][1], swapPosition3[2][1]

                mix.append(swapPosition1)
                mix.append(swapPosition2)
                mix.append(swapPosition3)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition3)

            elif currentList[2][2] == 0:
                swapPosition1 = copy.deepcopy(currentList)
                swapPosition1[2][2], swapPosition1[2][1] = swapPosition1[2][1], swapPosition1[2][2]

                swapPosition2 = copy.deepcopy(currentList)
                swapPosition2[2][2], swapPosition2[1][2] = swapPosition2[1][2], swapPosition2[2][2]

                mix.append(swapPosition1)
                mix.append(swapPosition2)

                parent.append(currentList)

                currentList = copy.deepcopy(swapPosition2)

            # In case all of that not happening
            else:
                print("some error in per-number")

        elif totalSimilar >= 2:
            # if currentList == mix[-1]:
            #     totalBackward += 1
            totalBackward += 1
            currentList = copy.deepcopy(mix[-totalBackward])

        else:
            print("some error occurrence at similar level")

        # Keep this in end first loop
        if loops == 0:
            mix.remove(mix[0])
            mix.insert(0, start)
            parent.remove(parent[0])
            # parent.insert(0, start)

        totalSimilar = 0

    elif currentList == end:
        print("Match this value at loop: ", loops, "\n")
        print("Start value: ")
        print(currentList, "\n")
        print("End value: ")
        print(end, "\n")

        break

    else:
        print("error occurrence at loops level")

print("All value of mix: ")
print(mix)

print("\nvalue of all matrix")
for x in mix:
    for y in x:
        print(y)
    print("\n")
