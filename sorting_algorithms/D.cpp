/*
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> merge_sort(vector<int> &a) {
    if (a.size() == 1) 
        return a;

    auto l1 = vector<int>(a.begin(), a.begin() + a.size() / 2);
    auto r1 = vector<int>(a.begin() + a.size() / 2, a.end());
    auto l = merge_sort(l1);
    auto r = merge_sort(r1);


    vector<int> res;
    merge(l.begin(), l.end(), r.begin(), r.end(), back_inserter(res));
    return res;
}


int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto& x : a) {
        cin >> x;
    }

    vector<int> res = merge_sort(a);

    for (auto c : res) {
        cout << c << " ";
    }
    cout << '\n';
} */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> a;
    int v;
    for (int x = 0; x < n; x++) {
        vector<int> temp;
        for (int y = 0; y < n; y++) {
            cin >> v;
            temp.push_back(v);
        }
        a.push_back(temp);
        temp.clear();
    }

    for (size_t i = 0; i < n - 1; i++) {
        auto min_idx = i;
        for (size_t j = i + 1; j < n; j++) {
            if (a[j][1] > a[min_idx][1]) {
                min_idx = j;
            }
        }
        swap(a[i], a[min_idx]);
    }

    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            cout << a[i][j] << ' ';
        }
        cout << '\n';
    }
}