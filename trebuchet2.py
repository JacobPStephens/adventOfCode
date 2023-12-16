f = open("trebuchet.in", "r")
testCases = [line.strip() for line in f]

d = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}
dkeys = d.keys()

def solve(testCase):

    minIndex = len(testCase)-1
    leftDigit = "0"

    maxIndex = 0
    rightDigit = "0"

    # check if every spelled out num in string
    for key in dkeys:
        if key in testCase:
            
            indexFound = testCase.index(key)

            # if minimum found
            if indexFound < minIndex:
                minIndex = indexFound
                leftDigit = d[key]

            # if maximum found
            if indexFound > maxIndex:
                maxIndex = indexFound
                rightDigit = d[key]

    # search from left side to minIndex to see if integer num exists
    for i in range(0, minIndex):
        if testCase[i].isnumeric():
            leftDigit = testCase[i]
            break

    # search from right side to maxIndex to see if integer num exists
    for i in range(len(testCase)-1, maxIndex, -1):
        if testCase[i].isnumeric():
            rightDigit = testCase[i]
            break
    
    return int(leftDigit + rightDigit)


total = 0   
for testCase in testCases:
    calibrationNum2 = solve(testCase)
    total += calibrationNum2

#52359
print(total)