num_lots = int(input())
yesterday = list(input())
today = list(input())
output = 0

for i in range(num_lots):
    if yesterday[i] == "C" and today[i] == "C":
        output += 1

print(output)