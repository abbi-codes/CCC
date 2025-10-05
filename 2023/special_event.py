num_people = int(input())
each_person = list()
all = [0, 0, 0, 0, 0]
output = ""

for i in range(num_people):
    availability = (list(input()))
    for j in range(5):
        if availability[j] == "Y":
            all[j] += 1

max_people_day = max(all)

for n in range(5):
    each = all[n]
    if each == max_people_day:
        output += str(n + 1) 
        output += ","

print(output[:len(output) - 1])