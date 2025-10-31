#include <bits/stdc++.h>
using namespace std;

int main()
{
    int question, n;
    cin >> question;
    cin >> n;
    int total_speed = 0;
    int d_speeds[100]={0}, p_speeds[100]={0};
    int lower_ndx, increment;

    for (int i=0; i < n; i++)
    {
        scanf("%d", &d_speeds[i]);
    }
    sort(d_speeds, d_speeds + n);

    for (int i=0; i < n; i++)
    {
        scanf("%d", &p_speeds[i]);
    }
    sort(p_speeds, p_speeds + n);
    
    if (question == 1) {
        lower_ndx = n - 1;
        increment = -1;
    }
    else {
        lower_ndx = 0;
        increment = 1;
    }
    int upper_ndx = n - 1;
    for (int i=0; i < n; i++)
    {
        total_speed += max(d_speeds[lower_ndx], p_speeds[upper_ndx]);
        lower_ndx += increment;
        upper_ndx -= 1;
    }

    cout << total_speed;
    return 0;
}