apples = [int(input()) for i in range(3)]
bananas = [int(input()) for i in range(3)]
app_score = apples[0] * 3 + apples[1] * 2 + apples[2]
ban_score = bananas[0] * 3 + bananas[1] * 2 + bananas[2]

if app_score > ban_score:
    print("A")
elif app_score < ban_score:
    print("B")
else:
    print("T")