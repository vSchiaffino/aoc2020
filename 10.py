from os import closerange


def main():
    adaptors = getAdaptors()
    adaptors.append(0)
    adaptors.sort()
    adaptors.append(adaptors[-1] + 3)
    differences = [0, 0, 0]
    last = adaptors[0]
    for adaptor in adaptors[1:]:
        diff = adaptor - last
        if(diff >= 4):
            print("what")
            return
        differences[diff - 1] += 1
        last = adaptor

    print(f"1 diff: {differences[0]}\n2 diff: {differences[1]}\n3 diff: {differences[2]}")
    print(f"Answer for the first puzzle: {differences[0] * differences[2]}")

def getAdaptors():
    with open("input.in", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            lines[i] = int(line.replace("\n", ""))
        return lines

if __name__ == "__main__":
    main()