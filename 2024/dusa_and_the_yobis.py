dusa_start_size = int(input())
current_size = dusa_start_size

while True:
    yobi = int(input())
    if yobi < current_size:
        current_size += yobi
    else:
        print(current_size)
        break    
