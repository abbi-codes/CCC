rows = int(input())
columns = int(input())
value_dollars = 0

for i in range(rows):
    pumpkins = input()
    for j in range(columns):
        pumpkin = pumpkins[j]
        if pumpkin == "S":
            value_dollars += 1
        elif pumpkin == "M":
            value_dollars += 5
        else:
            value_dollars += 10

print(value_dollars)    