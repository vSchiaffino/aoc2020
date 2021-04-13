import json
from copy import deepcopy

def main():
    seats = getSeats()
    lastSeats = deepcopy(seats)
    while(1):
        seats = round(seats)
        # show(seats)
        if(checkIfTheSeatsAreTheSame(seats, lastSeats)):
            break
        lastSeats = deepcopy(seats)
        
    print(countOccupiedSeats(seats))

def countOccupiedSeats(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1
    return count

def checkIfTheSeatsAreTheSame(seats1, seats2):
    if(len(seats1) != len(seats2) or len(seats1[0]) != len(seats1[0])):
        return False
    for i in range(len(seats1)):
        for j in range(len(seats1[i])):
            seat1 = seats1[i][j]
            seat2 = seats2[i][j]
            if(seat1 != seat2):
                return False
    return True


def show(seats):
    show = []
    for row in seats:
        showrow = ""
        for ch in row:
            showrow += ch
        show.append(showrow)
    print(json.dumps(show, indent=4))

def round(seats):
    final = deepcopy(seats)
    for i in range(len(seats)):
        row = seats[i]
        for j in range(len(row)):
            seat = row[j]
            if seat == "L":
                movs = [
                    #c, r
                    (0, -1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                    (0, 1),
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                ]
                makeChange = True
                for mov in movs:
                    seatAfterMov = applyMov(seats, [i, j], mov)
                    if(seatAfterMov != None):
                        if(seatAfterMov == "#"):
                            makeChange = False
                            break
                if makeChange:
                    final[i][j] = "#"
            elif seat == "#":
                occupiedCount = 0
                movs = [
                    #c, r
                    (0, -1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                    (0, 1),
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                ]
                for mov in movs:
                    seatAfterMov = applyMov(seats, [i, j], mov)
                    if(seatAfterMov != None):
                        if(seatAfterMov == "#"):
                            occupiedCount += 1
                            if(occupiedCount == 4):
                                final[i][j] = "L"
                                continue

    return final
                
def applyMov(seats, pos, mov):
    x = pos[0] + mov[1]
    y = pos[1] + mov[0]
    if x < 0 or x >= len(seats) or y < 0 or y >= len(seats[0]):
        return None
    return seats[x][y]

def getSeats():
    seats = []
    with open("input.in") as f:
        lines = f.readlines()
        for line in lines:
            finalrow = []
            row = line.replace("\n", "")
            for ch in row:
                finalrow.append(ch)
            seats.append(finalrow)
    return seats

if __name__ == "__main__":
    main()