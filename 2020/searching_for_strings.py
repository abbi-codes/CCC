needle = input()
needle_len = len(needle)
haystack = input()
haystack_len = len(haystack)
needle_specs = [0]*26
all_hashes = set()
my_list = [0]*26

if needle_len > haystack_len:
    print(0)
else:
    for ndx in range(needle_len):
        letter = haystack[ndx]
        my_list[ord(letter) - ord('a')] += 1
        needle_specs[ord(needle[ndx]) - ord('a')] += 1

    needle_specs = tuple(needle_specs)

    if tuple(my_list) == needle_specs:
        all_hashes.add(hash(haystack[:needle_len]))

    for i in range(haystack_len - needle_len):
        front_letter = haystack[i]
        last_letter = haystack[i + needle_len]
        if last_letter != front_letter:
            my_list[ord(last_letter) - ord('a')] += 1
            my_list[ord(front_letter) - ord('a')] -= 1
        if tuple(my_list) == needle_specs:
            all_hashes.add(hash(haystack[i + 1: i + needle_len + 1]))

    print(len(all_hashes))