n = int(input())
largest = (0, "")
for i in range(n):
    person = input()
    bid = int(input())
    if bid > largest[0]:
        largest = (bid, person)

print(largest[1])