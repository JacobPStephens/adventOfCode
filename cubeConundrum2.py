f = open("cubeConundrum.in", "r")
games = [line.strip() for line in f]

def solve(game):
    blueMax = -float('inf')
    greenMax = -float('inf')
    redMax = -float('inf')

    # find largest blue value
    blueCount = game.count('blue')
    startIndex = 0
    for i in range(blueCount):

        foundIndex = game.index('blue', startIndex, len(game))

        num = int(game[foundIndex-3:foundIndex].strip())
        if num > blueMax:
            blueMax = num

        startIndex = foundIndex + 1
    
    # find largest green value
    greenCount = game.count('green')
    startIndex = 0
    for i in range(greenCount):

        foundIndex = game.index('green', startIndex, len(game))

        num = int(game[foundIndex-3:foundIndex].strip())
        if num > greenMax:
            greenMax = num
        
        startIndex = foundIndex + 1

    # find largest red value
    redCount = game.count('red')
    startIndex = 0
    for i in range(redCount):
        foundIndex = game.index('red', startIndex, len(game))

        num = int(game[foundIndex-3:foundIndex].strip())
        if num > redMax:
            redMax = num
        
        startIndex = foundIndex + 1

    power = blueMax * greenMax * redMax
    return power

total = 0
for game in games:
    total += solve(game)

print(total)