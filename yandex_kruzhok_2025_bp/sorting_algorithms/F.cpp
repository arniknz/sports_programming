#include <bits/stdc++.h>

using namespace std;

void inssrt(vector<int> &a, int l, int r) {
    for (int i = l + 1; i <= r; i++) {
        int x = a[i];
        int j = i - 1;
        while (j >= l && a[j] > x) {
            a[j + 1]= a[j];
            j--;
        }
        a[j + 1] = x;
    }
}

int prt(vector<int> &a, int l, int r) {
    int m = l + (r - l) / 2;
    int p = a[m];
    int i = l, j = r;
    while (i < j) {
        while (a[i] < p) {i++;}
        while (a[j] > p) {j--;}
        if (i < j) {swap(a[i], a[j]); i++; j--;}
    }
    return i;
}

void qs(vector<int> &a, int l, int r) {
    stack<pair<int, int>> st;
    st.push({l, r});
    while (!st.empty()) {
        auto [ln, rn] = st.top();
        st.pop();
        if (ln >= rn) {continue;}
        if (rn - ln <= 30) {inssrt(a, ln, rn); continue;}
        int x = prt(a, ln, rn);
        if (x - ln > rn - x) {
            st.push({ln, x - 1});
            st.push({x + 1, rn});
        } else {
            st.push({x + 1, rn});
            st.push({ln, x - 1});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a) {cin >> x;}
    qs(a, 0, n - 1);
    for (auto x : a) {cout << x << " ";}
    cout << endl;
    return 0;
}