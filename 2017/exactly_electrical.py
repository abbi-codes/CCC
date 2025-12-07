import os

def run_test():
    start = list(map(int, input().strip().split()))
    destination =list(map(int, input().strip().split()))
    
    electrical_charge = int(input())
    total = abs(destination[0] - start[0]) + abs(destination[1] -  start[1])
    if electrical_charge >= total:
        if (electrical_charge - total) % 2 == 0:
            return 'Y'
        else:
            return 'N'
    else:
        return 'N'
    
print(run_test())