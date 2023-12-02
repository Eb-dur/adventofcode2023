

f = open("data")
d = f.readlines()
numbers = "0123456789"
res = 0

for line in d:
    one = ""
    two = ""
    for char in line:
        if char in numbers:
            one = char
            break
    for char in line[::-1]:
        if char in numbers:
            two = char
            break
    if one and two:
        res += int(one+two)
print(res)