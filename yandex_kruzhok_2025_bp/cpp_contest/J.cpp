#include <bits/stdc++.h>

using namespace std;

multimap<int, int> bs;
map<int, int> b;
void rm(const multimap<int, int>::iterator &i) {b.erase(i->second); bs.erase(i);}
void rmbs(const map<int, int>::iterator &i) {auto f = bs.find(i->second); while (f->second != i->first) {f++;} bs.erase(f); b.erase(i);}
void insrt(const pair<int, int> &p) {b.insert(p); bs.insert({p.second, p.first});}
int main() {
    int n, m, k, idx, s;
    cin >> n >> m;
    pair<int, int> p[m];
    insrt({1, n});
    for (auto i = 0; i < m; p[i] = {k, idx}, i++) {
        cin >> k;
        if (k > 0) {
            auto j = bs.lower_bound(k);
            if (j == bs.end()) {
                idx = -1;
            } else {
                idx = j->second;
                s = j->first - k;
                rm(j);
                if (s > 0) {insrt({idx + k, s});}
            }
            cout << idx << endl;
        } else {
            auto idx1 = p[abs(k) - 1].second;
            auto s1 = p[abs(k) - 1].first;
            if (idx1 == -1) {continue;}
            auto ir = b.lower_bound(idx1);
            auto il = (ir != b.begin()) ? prev(ir) : b.end();
            if (ir != b.end() && ir->first == idx1 + s1) {
                if (il != b.end() && il->first + il->second == idx1) {
                    idx = il->first;
                    s = il->second + ir->second;
                    rmbs(il);
                    rmbs(ir);
                    insrt({idx, s + s1});
                } else {
                    s = ir->second;
                    rmbs(ir);
                    insrt({idx1, s + s1});
                }
            } else {
                if (il != b.end() && il->first + il->second == idx1) {
                    idx = il->first;
                    s = il->second;
                    rmbs(il);
                    insrt({idx, s + s1});
                } else {
                    insrt({idx1, s1});
                }
            }
            idx = 0;
        }
    }
    return 0;
}