def type_of_day():
    month = int(input())
    day = int(input())
    if month == 2 and day == 18:
        return "Special"
    elif (month > 2):
        return "After"
    if month == 2 and day > 18:
        return "After"
    else:
        return "Before"

print(type_of_day())