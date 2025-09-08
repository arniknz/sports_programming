#include <bits/stdc++.h>

using namespace std;

void solve() {
    char mt[9][9];
    for (int i = 1; i <= 8; i++) {
        for (int j = 1; j <= 8; j++) {
            cin >> mt[i][j];
        }
    }

    int r = 0, c = 0;
    for (int i = 2; i <= 7; i++) {
        for (int j = 2; j <= 7; j++) {
            if (mt[i][j] == '#' && 
                mt[i - 1][j - 1] == '#' &&
                mt[i - 1][j + 1] == '#' &&
                mt[i + 1][j + 1] == '#' &&
                mt[i + 1][j - 1] == '#') {
                cout << i << " " << j << endl;
                return;
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt; cin >> tt; for (int i = 1; i <= tt; i++) {solve();}
}