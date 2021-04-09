def main():
    numbers = readNumbers()   
    print(getEncodingError(numbers))
    
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