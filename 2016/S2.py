question = int(input())
n = int(input())
d_speeds = list(map(int, input().split()))
p_speeds = list(map(int, input().split()))
total_speed = 0

d_speeds.sort()
p_speeds.sort()

if question == 1:
    lower_ndx = n - 1
    increment = -1
else:
    lower_ndx = 0
    increment = 1

upper_ndx = n - 1

for i in range(n):
    total_speed += max(d_speeds[lower_ndx], p_speeds[upper_ndx])
    lower_ndx += increment
    upper_ndx -= 1

print(total_speed)
