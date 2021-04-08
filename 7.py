import copy
import json
import numpy
"""

"""
sum = -1
def main():
    keyValues = {}
    with open("input.in", "r") as f:
        lines = f.readlines()
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
                    values.append({"color": color, "q": q})

            keyValues[key] = values
        
        count = 0
        for bag in keyValues:
            if(containsShinyBag(bag, keyValues)):
                count += 1
        print(count)
        print(qBagsInside("shiny gold", keyValues))


def containsShinyBag(key, allBags):
    childs = allBags[key]
    if childs is not None:
        for child in childs:
            if child["color"] == "shiny gold" or containsShinyBag(child["color"], allBags):
                return True
    return False

def qBagsInside(key, allBags):
    bagsInside = allBags[key]
    if(bagsInside is None):
        return 0
    count = 0
    for bag in bagsInside:
        count += bag["q"]
        count += (bag["q"] * qBagsInside(bag["color"], allBags))
    return count



    

        


        



if __name__ == "__main__":
    main()
