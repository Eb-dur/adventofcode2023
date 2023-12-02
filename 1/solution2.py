
f = open("data")
d = f.readlines()
numbers = "0123456789"
res = 0
stringNumbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six" : "6", "seven": "7", "eight": "8", "nine": "9"}

class Found(Exception):
    pass

for line in d:
    one = ""
    two = ""
    line = line.strip()
    try:
        for index in range(len(line)):
            if line[index] in numbers:
                one = line[index]
                break
            for stringNumber in stringNumbers:
                if line[index:].startswith(stringNumber):
                    one = stringNumbers[stringNumber]
                    raise Found
    except Found:
        pass
    try:
        for index in reversed(range(len(line))):
            if line[index] in numbers:
                two = line[index]
                break
            for stringNumber in stringNumbers:
                if line[index:].startswith(stringNumber):
                    two = stringNumbers[stringNumber]
                    raise Found
    except Found:
        pass
        
    if one and two:
        res += int(one+two)
print(res)