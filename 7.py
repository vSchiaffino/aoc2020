import copy
"""
gold
    dark olive
        3 faded blue
        4 dotted black
    2 vibrant plum
        5 faded blue
        6 dotted black
"""
sum = -1
def main():
    with open("input.in", "r") as f:
        lines = f.readlines()
        keyValues = {}
        for line in lines:
            line = line.replace("\n", "").replace(".", "")
            parts = line.split(" bags contain ")
            key = parts[0]
            str_values = parts[1].split(", ")
            values = []
            if str_values == ["no other bags"]:
                values = None
            else:
                for value in str_values:
                    sep_value = value.split(" ")
                    q = int(sep_value[0])
                    color_list = sep_value[1:-1]
                    color = " ".join(color_list)
                    values.append({"q": q, "color": color})

            keyValues[key] = values
        countingBags = getAllTheBagsInside("shiny gold", keyValues)
        final = []
        for bag in countingBags:
            if bag not in final and bag != "shiny gold":
                final.append(bag)
        print(len(final))
    
def getAllTheBagsInside(key, allBags):
    # print(key)
    # print("    ", end="")
    bagsInside = []
    childBags = allBags[key]
    bagsInside.append(key)
    if childBags is not None:
        for childBag in childBags:
            values = getAllTheBagsInside(childBag["color"], allBags)
            print(f"{childBag['color']} {values}")
            bagsInside.extend(values)
        print("--")

    return bagsInside

        



if __name__ == "__main__":
    main()
