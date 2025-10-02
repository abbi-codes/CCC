#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int m = 0;
    vector<int> all_data;
    string letter_s = "S";
    for (int i = 0; i < n; i++) {
        string s_or_p;
        cin >> s_or_p;
        if (s_or_p == letter_s) {
            all_data.push_back(1);
        } 
        else {
            all_data.push_back(0);
        }
    }
    int curr_max;
    for (int j = 0; j < n; j++) {
        if (all_data[j] == 0) {
            all_data[j] = 1;
            int most_max = 0;
            int my_curr_max = 0;
            for (int a = 0; a < n; a++) {
                if (all_data[a] == 1) {
                    my_curr_max += 1;
                }
                else if (all_data[a] == 0) {
                    my_curr_max = 0;
                }
                if (my_curr_max >= most_max) {
                    most_max = my_curr_max;
                }
            }
            curr_max = most_max;
            all_data[j] = 0;
        }
        else {
            all_data[j] = 0;
            int most_max = 0;
            int my_curr_max = 0;
            for (int a = 0; a < n; a++) {
                if (all_data[a] == 1) {
                    my_curr_max += 1;
                }
                else if (all_data[a] == 0) {
                    my_curr_max = 0;
                }
                if (my_curr_max >= most_max) {
                    most_max = my_curr_max;
                }
            }
            curr_max = most_max;
            all_data[j] = 1;
        }
        if (curr_max > m) {
            m = curr_max;
            curr_max = 0;
        }
    }
    cout << m;
    return 0;
}