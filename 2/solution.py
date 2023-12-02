f = open("data")
d = f.readlines()

res = 0

for line in d:
    semi = line.find(":")
    firstSpace = line.find(" ")
    Id = line[firstSpace+1:semi]
    rolls = line[semi+1:]
    rolls = rolls.strip()
    rolls = rolls.split("; ")
    possible = True
    for subroll in rolls:
        red = 12
        green = 13
        blue = 14
        subroll = subroll.split(", ")
        for item in subroll:
            firstSpace = item.find(" ")
            match item[firstSpace+1:]:
                case "blue":
                    blue -= int(item[:firstSpace])
                case "green":
                    green -= int(item[:firstSpace])
                case "red":
                    red -= int(item[:firstSpace])

        if red < 0 or green < 0 or blue < 0:
            possible = False
    if possible:
        print("Possible: " + Id)
        res += int(Id)
    else: print("Impossible: " + Id)

print(res)

