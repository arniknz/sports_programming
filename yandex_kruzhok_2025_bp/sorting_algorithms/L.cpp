#include <bits/stdc++.h>

using namespace std;

bool is_pal(string a) {
    string b = a;
    reverse(a.begin(), a.end());
    return a == b;
}

bool ok(string a) {
    int cnt[26] = {0};
    for (auto x : a) {cnt[x - 'A']++;}
    int o = 0;
    for (int i = 0; i < 26; i++) {if (cnt[i] % 2 != 0) {o++;}}
    if (a.size() % 2 == 0) {if (o > 0) {return false;} else {return true;}}
    if (o != 1) {return false;}
    return true;
}

string mk_pal(string a) {
    int cnt[26] = {0};
    for (auto x : a) {cnt[x - 'A']++;}
    string s;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] % 2 != 0) {cnt[i]--; s += (char)(i + 'A'); break;}
    }
    string bok1, bok2;
    for (int i = 0; i < 26; i++) {
        string tmp;
        if (cnt[i] != 0) {
            char c = (char)(i + 'A');
            for (int j = 0; j < cnt[i] / 2; j++) {
                tmp += c;
            }
            bok1 += tmp;
            bok2 = tmp + bok2;
        }
    }
    return bok1 + s + bok2;
}

int main() {
    int n;
    string a;
    cin >> n >> a;
    if (is_pal(a)) {cout << a << endl; return 0;}
    vector<string> ans;
    for (int i = 0; i < n; i++) {
        string p;
        for (int j = i; j < n; j++) {p += a[j]; if (ok(p)) {ans.push_back(mk_pal(p));}}
    }
    if (!ans.empty()) {
        string res;
        size_t mx = 0;
        for (auto x : ans) {
            if (x.length() > mx) {mx = x.length();}
        }
        for (auto x : ans) {
            if (x.length() == mx) {if (res.empty() || x < res) {res = x;}}
        }
        cout << res << endl;

    } else {cout << a[0] << endl;}
    return 0;
}