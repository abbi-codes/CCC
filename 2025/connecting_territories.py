r = int(input())
c = int(input())
m = int(input())
row_1 = []
row_2 = []
counter = 1
minimum_cost = 10000000
curr_cost = 10000000

for i in range(2):
    if i == 0:
        for j in range(c):
            row_1.append(counter)
            if counter == m:
                counter = 1
            else:
                counter += 1
    else:
        for k in range(c):
            row_2.append(counter)
            if counter == m:
                counter = 1
            else:
                counter += 1

for a in range(c):
    for b in range(c):
        if (a == b) or (b == a + 1) or (b == a - 1):
            curr_cost = row_1[a] + row_2[b]
            if curr_cost < minimum_cost:
                minimum_cost = curr_cost
print(minimum_cost)