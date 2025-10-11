begin_boil = int(input())
atmos_press = 5 * begin_boil - 400

print(atmos_press)

if atmos_press < 100:
    print(1)
elif atmos_press == 100:
    print(0)
else:
    print(-1)