output = []
while True:
    secret = input()
    instructon = secret[:2]
    sum = int(instructon[0]) + int(instructon[1])
    if secret == "99999":
        break
    elif sum != 0 and sum % 2 == 0:
        previous = "right"
        output.append(f"right {secret[2:]}")
    elif sum == 0:
        output.append(f"{previous} {secret[2:]}")
    else:
        previous = "left"
        output.append(f"left {secret[2:]}")

for i in output:
    print(i)