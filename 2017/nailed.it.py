n = int(input())
pieces_of_wood = list(map(int, input().split()))
woods_present = [0] * 2001
poss_lens = [0]* 4001

for piece in pieces_of_wood:
    woods_present[piece] += 1

for i in range(1, 2001):
    num_of_wood1 = woods_present[i]
    if num_of_wood1 == 0:
        continue
    poss_lens[i * 2] += num_of_wood1 // 2
    for j in range(i+1, 2001):
        num_of_wood2 = woods_present[j]
        if num_of_wood2 == 0:
            continue
        poss_lens[i + j] += min(num_of_wood1, num_of_wood2)

longest_fence = max(poss_lens)
print(longest_fence, poss_lens.count(longest_fence))