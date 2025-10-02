n = int(input())
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
code = []
processed_code = []

for i in range(n):
    code = ""
    num = 0
    input_code = input()
    j = 0
    while j < len(input_code):
        digit = input_code[j]
        if digit in lower_case:
            j += 1
            continue
        elif digit in upper_case:
            code += input_code[j]
            j += 1
        else:
            new_ndx = j + 1
            while True:
                if new_ndx >= len(input_code):
                    new_ndx += 1
                    j = new_ndx
                    break
                if input_code[new_ndx] == "-":
                    num += int(digit)
                    digit = "-"
                    new_ndx += 1
                    j = new_ndx
                elif ((input_code[new_ndx]) not in upper_case) and ((input_code[new_ndx]) not in lower_case):
                    digit += input_code[new_ndx]
                    new_ndx += 1
                else:
                    j = new_ndx
                    break
                
            num += int(digit)
    
    print(code + str(num))