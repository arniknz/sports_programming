#include <bits/stdc++.h>

using namespace std;

deque<int> bok1, bok2;

void eq() {
    if (bok1.size() < bok2.size()) {
        bok1.push_back(bok2.front());
        bok2.pop_front();
    } else if (bok1.size() > bok2.size() + 1) {
        bok2.push_front(bok1.back());
        bok1.pop_back();
    }
}

int main() {
    int n, i;
    char a;
    cin >> n;
    while (n--) {
        cin >> a;
        if (a == '+') {
            cin >> i;
            bok2.push_back(i);
        } else if (a == '*') {
            cin >> i;
            bok1.push_back(i);
        } else {
            cout << bok1.front() << endl;
            bok1.pop_front();
        }
        eq();
    }
    return 0;
}