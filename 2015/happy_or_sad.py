line_input = input()
happy_count = line_input.count(":-)")
sad_count = line_input.count(":-(")

if happy_count > sad_count:
    print("happy")

elif happy_count < sad_count:
    print("sad")

elif happy_count == 0 and sad_count == 0:
    print("none")

else:
    print("unsure")