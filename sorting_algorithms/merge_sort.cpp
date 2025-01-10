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
}