from random import shuffle

numList = list(range(1, 91))
calledNum = []

shuffle(numList)  # Shuffle once at start

while True:
    draw = input("Press any key to call out a number or 's' to stop: ").lower()

    if draw == "s":
        print("Game stopped.")
        break

    if len(numList) == 0:
        print("All numbers have been called!")
        break

    drawnNum = numList.pop()
    print("Number called:", drawnNum)

    calledNum.append(drawnNum)
    print("Numbers called so far:", calledNum)
