import json
# byr iyr eyr hgt hcl ecl pid - cid
def main():
    passports = getPassports()
    # print(json.dumps(passports, indent=4))
    validPassports = 0
    for passport in passports:
        validPassports += validatePassport(passport)
    print(validPassports)

def validatePassport(passport):
    # ------- byr
    byr = passport.get("byr", "0")
    byr_i = int(byr)
    if len(byr) != 4 or byr_i < 1920 or byr_i > 2002:
        return 0
    # ------- iyr
    iyr = passport.get("iyr", "0")
    iyr_i = int(iyr)
    if len(iyr) != 4 or iyr_i < 2010 or iyr_i > 2020:
        return 0
    # ------- eyr
    eyr = passport.get("eyr", "0")
    eyr_i = int(eyr)
    if len(eyr) != 4 or eyr_i < 2020 or eyr_i > 2030:
        return 0
    # ------- hgt
    hgt = passport.get("hgt", "0cm")
    try:
        hgt_val = int(hgt[:-2])
    except:
        print("error hgt")
        return 0
    hgt_type = hgt[-2:]
    if (hgt_type == "cm" and (hgt_val < 150 or hgt_val > 193)) or (hgt_type == "in" and (hgt_val < 59 or hgt_val > 76)):
        return 0
    # ------- hcl
    hcl = passport.get("hcl", "")
    if len(hcl) != 7:
        return 0
    else:
        for c in hcl[1:]:
            valid = "0123456789abcdef"
            if c not in valid:
                return 0
    # ------- ecl
    ecl = passport.get("ecl", "")
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in valid:
        return 0
    # ------ pid
    pid = passport.get("pid", "")
    if(len(pid) != 9):
        return 0
    else:
        try:
            pid_i = int(pid)
        except:
            print("error pid")
            return 0
    # --- valid
    return 1

def getPassports():
    with open("input.in", "r") as f:
        passports = []
        passport = {}
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                passports.append(passport)
                passport = {}
            else:
                keyValues = line.split(" ")
                for keyValue in keyValues:
                    separated = keyValue.split(":")
                    key = separated[0]
                    value = separated[1].replace("\n", "")
                    passport[key] = value
        passports.append(passport)
        return passports



if __name__ == "__main__":
    main()