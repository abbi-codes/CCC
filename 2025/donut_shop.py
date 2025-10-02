d = int(input())
e = int(input())
r = d

for i in range(e):
    add_or_sub = input()
    num_donuts = int(input())
    if add_or_sub == "+":
        r += num_donuts
    else:
        r -= num_donuts

print(r)