num_participants = int(input())
scores = []
num_bronze = 0

for i in range(num_participants):
    given_input = int(input())
    scores.append(given_input)

gold_score = max(scores)
silver_score = 0

for j in range(num_participants):
    curr_score = scores[j]
    if (curr_score < gold_score) and (curr_score > silver_score):
        silver_score = curr_score

bronze_score = 0

for k in range(num_participants):
    curr_score = scores[k]
    if (curr_score < silver_score) and (curr_score > bronze_score):
        bronze_score = curr_score

for l in range(num_participants):
    curr_score = scores[l]
    if curr_score == bronze_score:
        num_bronze += 1

print(bronze_score, num_bronze)