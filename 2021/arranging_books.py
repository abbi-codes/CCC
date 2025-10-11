def find_letter_pos(start_ndx, end_ndx, book_size):
    for loc in range(start_ndx, end_ndx):
        book = shelf_of_books[loc]
        if book == 'L':
            l_present_now[book_size] += 1
        elif book == 'M':
            m_present_now[book_size] += 1
        else:
            s_present_now[book_size] += 1


shelf_of_books = input()
num_larges = shelf_of_books.count('L')
num_mediums = shelf_of_books.count('M')
num_smalls = shelf_of_books.count('S')
l_present_now = [0, 0, 0]
m_present_now = [0, 0, 0]
s_present_now = [0, 0, 0]


find_letter_pos(0, num_larges, 0)
find_letter_pos(num_larges, num_larges + num_mediums, 1)
find_letter_pos(num_larges + num_mediums, num_larges + \
num_mediums + num_smalls, 2)


# compute_swaps:
min_l_and_m_swap = min(l_present_now[1], m_present_now[0])
min_m_and_s_swap = min(m_present_now[2], s_present_now[1])
min_l_and_s_swap = min(l_present_now[2], s_present_now[0])


l_present_now[1] -= min_l_and_m_swap
l_present_now[2] -= min_l_and_s_swap


min_swaps = min_l_and_m_swap + min_m_and_s_swap + \
min_l_and_s_swap + (l_present_now[1] + l_present_now[2]) * 2


print(min_swaps)