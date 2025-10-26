#include <bits/stdc++.h>

using namespace std;

const int MAXCL = 1e5;
int used[MAXCL] = {0};

map<int, int> mk(vector<pair<int, int>> &g) {
    map<int, int> gr;
    for (auto x : g) {gr[x.first] = x.second;}
    return gr;
}

int main() {
    int n, cnt = 0; cin >> n;
    vector<pair<int, int>> g;
    for (auto i = 1; i <= n; i++) {
        int v; cin >> v;
        g.push_back({i, v});
    }

    map<int, int> gr = mk(g);
    for (auto i = 1; i <= n; i++) {
        if (!used[i]) {
            int c = i;
            while (!used[c]) {
                used[c] = i;
                c = gr[c];
            }
            if (used[c] == i) {cnt++;}
        }
    }
    cout << cnt << endl;
    return 0;
}