f = open("data")
d = f.readlines()
res = 0

for line in d:
    semi = line.find(":")
    firstSpace = line.find(" ")
    rolls = line[semi+1:]
    rolls = rolls.strip()
    rolls = rolls.split("; ")
    red = 0
    green = 0
    blue = 0
    for subroll in rolls:
        subroll = subroll.split(", ")
        for item in subroll:
            firstSpace = item.find(" ")
            match item[firstSpace+1:]:
                case "blue":
                    amount = int(item[:firstSpace])
                    if amount > blue:
                        blue = amount
                case "green":
                    amount = int(item[:firstSpace])
                    if amount > green:
                        green = amount
                case "red":
                    amount = int(item[:firstSpace])
                    if amount > red:
                        red = amount
    pwr = red * green * blue
    res += pwr
print(res)
        
