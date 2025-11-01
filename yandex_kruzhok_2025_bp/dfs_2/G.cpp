#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;
const int MAXN = 1e6;
bool used[MAXN] = {false};
int h[MAXN], d[MAXN];
map<int, vector<pair<int, int>>> g;
vector<bool> most(MAXN, false);
vector<int> comp(MAXN, -1);
int comp_cnt = 0;

void bridges(int v, int p = -1, int id = -1) {
    used[v] = true;
    d[v] = h[v] = (p == -1 ? 0 : h[p] + 1);
    for (auto &[u, i] : g[v]) {
        if (i == id) {continue;}
        if (used[u]) {
            d[v] = min(d[v], h[u]);
        } else {
            bridges(u, v, i);
            d[v] = min(d[v], d[u]);
            if (h[v] < d[u]) {
                most[i] = true;
            }
        }
    }
}

void comps(int v, int id) {
    comp[v] = id;
    for (auto &[u, i] : g[v]) {
        if (comp[u] == -1 && !most[i]) {
            comps(u, id);
        }
    }
}

int main() {
    int n, m; cin >> n >> m;
    for (auto i = 1; i <= m; i++) {
        int u, v; cin >> u >> v;
        g[u].push_back({v, i}); g[v].push_back({u, i});
    }
    for (auto i = 1; i <= n; i++) {if (!used[i]) {bridges(i);}}
    for (auto i = 1; i <= n; i++) {if (comp[i] == -1) {comps(i, comp_cnt++);}}
    vector<int> cmp_sz(comp_cnt, 0);
    for (auto i = 1; i <= n; i++) {
        if (comp[i] != -1) {cmp_sz[comp[i]]++;}
    }
    vector<set<int>> bt(comp_cnt);
    for (auto i = 1; i <= n; i++) {
        for (auto &[u, id] : g[i]) {
            if (comp[i] != comp[u]) {
                bt[comp[i]].insert(comp[u]);
                bt[comp[u]].insert(comp[i]);
            }
        }
    }
    int k = 0;
    long long c = 1;
    for (auto i = 0; i < comp_cnt; i++) {
        if (bt[i].size() == 1) {
            k++;
            c = (c * cmp_sz[i]) % MOD;
        }
    }
    if (comp_cnt == 1) {k = 1; c = n;}
    cout << k << " " << c << endl;
    return 0;
}