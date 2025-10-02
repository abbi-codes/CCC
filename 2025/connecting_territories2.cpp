#include <bits/stdc++.h>

using namespace std;

int find_thing() {

    return 0;
}


int main() {
    int r;
    cin >> r;
    int c;
    cin >> c;
    int m;
    cin >> m;
    vector<vector<int>> grid;
    int counter = 1;
    int minimum_cost = 1000000000000;
    int curr_cost = 1000000000000;

    for (int i = 0; i < r; i++) {
        vector<int> vec_for_grid(c);
        for (int j; j < c; j++) {
            if (counter == m) {
                counter = 1;
                vec_for_grid.push_back(counter);
            }
            else {
                counter += 1
            }

        }
        }
    }

for i in range(2):
    if i == 0:
        for j in range(c):
            row_1.append(counter)
            if counter == m:
                counter = 1
            else:
                counter += 1
    else:
        for k in range(c):
            row_2.append(counter)
            if counter == m:
                counter = 1
            else:
                counter += 1

for a in range(c):
    for b in range(c):
        if (a == b) or (b == a + 1) or (b == a - 1):
            curr_cost = row_1[a] + row_2[b]
            if curr_cost < minimum_cost:
                minimum_cost = curr_cost
print(minimum_cost)


    return 0;
}