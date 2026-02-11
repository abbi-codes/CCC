#include <bits/stdc++.h>

int main() {
    int num_rows;
    int num_cols;
    std::cin >> num_rows;
    std::cin >> num_cols;

    std::vector<std::vector<int>> room(num_rows, std::vector<int>(num_cols));

    for (int i = 0; i < num_rows; i++) {
        for (int j = 0; j < num_cols; j++) {
            scanf("%d", &room[i][j]);
        }
    }

    std::unordered_map<int, std::vector<int>> my_map;
    for (int row = 0; row < num_rows; row++) {
        for (int col = 0; col < num_cols; col++) {
            int coord_num = (row+1)*(col+1);
            if (my_map.find(coord_num) == my_map.end()) {
                my_map[coord_num] = std::vector<int>();
            }
            if ((row == num_rows - 1) && (col == num_cols - 1)) {
                my_map[coord_num].push_back(-1);
            }
            my_map[coord_num].push_back(room[row][col]);
        }
    }

    std::queue<std::vector<int>> my_queue;
    my_queue.push(my_map[1]);
    std::vector<bool> all_points_visited(1000001, false);

    while (true) {
        if (my_queue.empty()) {
            std::cout << "no" << std::endl;
            return 0;
        }
        auto sub_points = my_queue.front();
        for (auto next_point : sub_points) {
            if (next_point == -1) {
                std::cout << "yes" << std::endl;
                return 0;
            }
            if (!all_points_visited[next_point]) {
                all_points_visited[next_point] = true;
                if (my_map.find(next_point) == my_map.end()) {
                    continue;
                }
                my_queue.push(my_map[next_point]);
            }
        }
        my_queue.pop();
    }
    return 0;
}
