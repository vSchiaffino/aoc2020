def main():
    with open("input.in", "r") as f:
        lines = f.readlines()
        # count = 0
        # groupCount = 0
        # groupAlreadyAfirmed = ""
        # for line in lines:
        #     if line == "\n":
        #         # print(groupAlreadyAfirmed, groupCount)
        #         groupAlreadyAfirmed = ""
        #         groupCount = 0
        #         continue
        #     else:
        #         line = line[:-1]
        #         for c in line:
        #             if c not in groupAlreadyAfirmed:
        #                 groupAlreadyAfirmed += c
        #                 groupCount += 1
        #                 count += 1
        # print(count)
        groups = []
        group = []
        for line in lines:
            if line == "\n":
                groups.append(group)
                group = []
                continue
            else:
                line = line[:-1]
                group.append(line)
        groups.append(group)

        count = 0
        allLeters = "abcdefghijklmnopqrstuvwxyz"
        for group in groups:
            everyoneYes = "abcdefghijklmnopqrstuvwxyz"
            for person in group:
                for l in allLeters:
                    if l in person:
                        continue
                    else:
                        everyoneYes = everyoneYes.replace(l, "")
            # print(everyoneYes)
            count += len(everyoneYes)
        print(count)





if __name__ == "__main__":
    main()