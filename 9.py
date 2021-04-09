def main():
    numbers = readNumbers()   
    encodingError = getEncodingError(numbers)
    print(encodingError)
    weakness = findWeakness(numbers, encodingError)
    print(weakness)

def findWeakness(numbers, encodingError):
    for i, number in enumerate(numbers):
        sum = 0
        j = i
        while 1:
            if  j >= len(numbers):
                break
            sum += numbers[j]
            if(sum == encodingError):
                sumNumbers = numbers[i:j + 1]
                sumNumbers.sort()
                _max = sumNumbers[-1]
                _min = sumNumbers[0]
                return _max + _min
            elif sum > encodingError:
                break
            j += 1

def getEncodingError(numbers, preambleLength = 25):
    lastNumbers = []
    for number in numbers:
        if len(lastNumbers) < preambleLength:
            lastNumbers.append(number)
        else:
            if (not checkEncodingError(number, lastNumbers)):
                return number
            lastNumbers.remove(lastNumbers[0])
            lastNumbers.append(number)

def checkEncodingError(number, lastNumbers):
    for i, num1 in enumerate(lastNumbers[:-1]):
        for num2 in lastNumbers[i + 1:]:
            if num1 + num2 == number:
                return True
    return False

def readNumbers():
    numbers = []
    with open("input.in", "r") as f:
        lines = f.readlines()
        for line in lines:
            numbers.append(int(line.replace("\n", "")))
    return numbers


if __name__ == "__main__":
    main()