num_people = int(input())
day_zero = int(input())
each_day = int(input())
day = 0
infected = day_zero
previous = day_zero
while infected <= num_people:
    day += 1
    infected += previous * each_day
    previous = previous * each_day
print(day)