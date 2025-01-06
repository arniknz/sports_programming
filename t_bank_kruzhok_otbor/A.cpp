#include <iostream>
#include <math.h>

using namespace std;

struct ans {
    int a;
    int b;
    int c;
    int d;
};

ans solve(int n) {
    auto l = sqrt(n) + 1;
    for (auto a = 0; a <= l; a++) {
        for (auto b = 0; b <= l; b++) {
            for (auto c = 0; c <= l; c++) {
                for (auto d = 0; d <= l; d++) {
                    if (a * a + b * b + c * c + d * d == n) {
                        return {a, b, c, d};
                    }
                }
            }
        }
    }
}

int main() {
    int n;
    cin >> n;

    ans ans = solve(n);

    cout << ans.a << " " << ans.b << " " << ans.c << " " << ans.d << '\n';
}