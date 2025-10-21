num_lines = int(input())
output = []

for i in range(num_lines):
    line = input()
    current = []
    times = 0
    occuring_char = line[0]
    for char in line:
        if char == occuring_char:
            times += 1
        else:
            current.append(str(times))
            current.append(occuring_char)
            occuring_char = char
            times = 1
    current.append(str(times))
    current.append(occuring_char)
    output.append(current)

for out in output:
    print(" ".join(out))