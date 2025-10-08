n = int(input())
is_gold = 0
is_gold_team = True

for num in range(n):
    points = int(input())
    fouls = int(input())
    score = points * 5 - fouls * 3
    if score <= 40:
        is_gold_team = False
    else:
        is_gold += 1

if is_gold_team:
    print(str(is_gold) + "+")

else:
    print(is_gold)
