#include <deque>
#include <iostream>
#include <vector>
#include <algorithm>

#define ll long long
#define deq deque<int>

using namespace std;

vector<ll> cnt_sort(int n, vector<ll> &a) {
    ll mx = *max_element(a.begin(), a.end());
    vector<ll> cnt(mx + 1, 0);

    for (auto e: a) {
        cnt[e]++;
    }

    auto b = 0;
    for (int i = 0; i < mx + 1; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            a[b++] = i;
        }
    }

    return a;
}

int main() {
    int n;
    cin >> n;
    deq ochered;
    while (n--) {

    }
    return 0;
}