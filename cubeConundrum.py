f = open("cubeConundrum.in", "r")
games = [line.split(":")[1].strip() for line in f]

redMax = 12
greenMax = 13
blueMax = 14

def solve(game, gameID):
    # separate pulls by semi-colon
    pulls = game.split(";")

    for pull in pulls:
        # each pair in pull separated by comma
        pairs = pull.split(",")

        for pair in pairs:
            num = int(pair.strip().split()[0])

            # see if number higher than maxes
            # if it is, return 0
            if num > blueMax:
                return 0
            elif (num > greenMax) and (pair.split()[1] == "green"):
                return 0
            elif (num > redMax) and (pair.split()[1] == "red"):
                return 0

    # if every pull hasn't returned yet,
    # the game is valid, so return its ID
    return gameID

# iterate through every game, keeping track 
# of total valid game IDs
total = 0
gameID = 1
for game in games:
    total += solve(game, gameID)
    gameID += 1

print(total)