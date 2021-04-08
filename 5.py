import json
def main():
    with open("input.in", "r") as f:
        lines = f.readlines()
        seatsIds = []
        seats = []
        rows = []
        for i in range(128):
            rows.append([0, 0, 0, 0, 0, 0, 0, 0])
        for line in lines:
            seat = getSeat(line[:-1])
            rows[seat[0]][seat[1]] = 1
            seats.append(seat)
            seatsIds.append(getSeatId(seat))
        seatsIds.sort()
        # print(seats[-1]) #part1
        finalRows = []
        i = 0
        for row in rows:
            if 0 in row:
                row.append(f"---{i}----")
                finalRows.append(row)
            i += 1

                
        print(json.dumps(finalRows, indent=4))
        # i = seatsIds[0]
        # rows = 
        # for seat in seatsIds:
        #     if(i != seat):
        #         i = seat - 1
        #         print(seat)
        #     i += 1
            

def getSeatId(seat):
    return seat[0] * 8 + seat[1]

def getSeat(indications):
    return [getSeatRow(indications[:7]), getSeatColumn(indications[7:])]

def getSeatRow(indications):
    # indications = FBFBBFF -> 7
    row = 0
    totalPossibilities = 128
    for letter in indications:
        if letter == "F":
            pass
        elif letter == "B":
            row += totalPossibilities // 2
        totalPossibilities = totalPossibilities // 2
    return row

def getSeatColumn(indications):
    column = 0
    totalPossibilities = 8
    for letter in indications:
        if letter == "L":
            pass
        elif letter == "R":
            column += totalPossibilities // 2
        totalPossibilities = totalPossibilities // 2
    return column

if __name__ == "__main__":
    main()