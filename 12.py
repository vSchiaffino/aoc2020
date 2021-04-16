def main():
    actions = getActions()
    print(getManhattanDistance(actions))

def getManhattanDistance(actions):
    pos = [0, 0]
    facing = 90
    convertFacingToDirection = {0: "N", 90: "E", 180: "S", 270: "W"}
    convertTowardsToSign = {"L": -1, "R": 1}
    for action in actions:
        t = action["action"]
        v = action["value"]
        # print(f"{t} {v}")
        if t == "R" or t == "L":
            facing += (convertTowardsToSign[t] * v)
            facing = facing % 360
        if t == "F":
            t = convertFacingToDirection[facing]
        if t == "N":
            pos[1] += v
        elif t == "S":
            pos[1] -= v
        elif t == "E":
            pos[0] += v
        elif t == "W":
            pos[0] -= v
        # print(f"{pos} {convertFacingToDirection[facing]}")

    return abs(pos[0]) + abs(pos[1])



def getActions():
    actions = []
    with open("input.in") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            action = line[0]
            value = int(line[1:])
            actions.append({"action": action, "value": value})
    return actions


if __name__ == "__main__":
    main()