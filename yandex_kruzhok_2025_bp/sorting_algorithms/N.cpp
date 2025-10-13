#include <bits/stdc++.h>

using namespace std;

struct kis {
    int idx;
    double a, b;
};

struct cmp {
    bool operator()(const kis &a, const kis &b) const {return a.a/a.b > b.a/b.b;}
};

int main() {
    int n;
    cin >> n;
    vector<kis> ans(n);
    for (int i = 0; i < n; i++) {
        ans[i].idx = i + 1;
        cin >> ans[i].a >> ans[i].b;
    }
    sort(ans.begin(), ans.end(), cmp());
    double res = 0.0;
    int l = 0, r = ans.size() - 1;
    while (l < r) {
        if (ans[l].a < ans[r].b) {
            ans[r].a = ans[r].a * (ans[r].b - ans[l].a) / ans[r].b;
            ans[r].b = ans[r].b - ans[l].a;
            res += ans[l].a;
            l++;
        } else {
            ans[l].b = ans[l].b * (ans[l].a - ans[r].b) / ans[l].a;
            ans[l].a = ans[l].a - ans[r].b;
            res += ans[r].b;
            r--;
        }
        if (ans[l].a == 0) {l++;}
        if (ans[r].b == 0) {r--;}
    }
    if (l == r) {res += (ans[l].a * ans[l].b)/(ans[l].a + ans[l].b);}
    cout << fixed << setprecision(6) << res << endl;
    for (auto x : ans) {
        cout << x.idx << " ";
    }
    cout << endl;
    return 0;
}