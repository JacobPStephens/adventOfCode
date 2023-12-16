f = open("trebuchet.in", "r")
testCases = [line.strip() for line in f]

def solve(testCase):

    # iterate through forwards
    for ch in testCase:
        # break once you find first number
        if ch.isnumeric():
            firstDigit = ch
            break

    # iterate through backwards
    for i in range(len(testCase)-1, -1, -1):
        # break once you find last number
        if testCase[i].isnumeric():
            lastDigit = testCase[i]
            break

    # return calibration value for every case
    return int(firstDigit + lastDigit)

# increment total by calibration value for every case
total = 0   
for testCase in testCases:
    total += solve(testCase)

print(total)