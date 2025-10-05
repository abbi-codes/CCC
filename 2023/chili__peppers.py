num_peppers = int(input())
all_pep_val = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000}
total = 0

for i in range(num_peppers):
    pepper = input()
    total += all_pep_val[pepper]

print(total)