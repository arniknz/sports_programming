#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> m(3);
    for (auto &x: m) {
        cin >> x;
    }


    int a = 1;
    for (auto c: m) {
        if (c < n && c > a) {
            a = c;
        }
    }
    cout << a << '\n';
}