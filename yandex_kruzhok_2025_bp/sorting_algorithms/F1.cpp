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
    int m = (r + l) / 2;
    int p = a[m];
    int i = l, j = r;
    while (i <= j) {
        while (a[i] < p) {i++;}
        while (a[j] > p) {j--;}
        if (i >= j) {break;}
        swap(a[i++], a[j--]);
    }
    return j;
}

void qs(vector<int> &a, int l, int r) {
    if (l < r) {
        if (r - l <= 10) {inssrt(a, l, r); return;}
        int x = prt(a, l, r);
        qs(a, l, x);
        qs(a, x + 1, r);
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