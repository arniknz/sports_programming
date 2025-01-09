#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    unsigned long long k;
    cin >> k;

    unsigned long long m = (unsigned long long)pow(10, 12);
    unsigned long long p1 = 1;
    for (unsigned long long i = 2; i < m; i++) {
        if (k == 1) {
            cout << 1 << '\n';
            break;
        }
        if ((p1 * i) % k == 0) {
            cout << i << '\n';
            break;
        }
        p1 = (p1 * i) % k;
    }
}

/*
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    unsigned long long k;
    cin >> k;

    unsigned long long m = (unsigned long long)pow(10, 12);

    vector<unsigned long long> p = {0, 1};
    for (unsigned long long i = 2; i < m; i++) {
        if (k == 1) {
            cout << 1 << '\n';
            break;
        }

        if ((p[i - 1] * i) % k == 0) {
            cout << i << '\n';
            break;
        }
        p.push_back((p[i - 1] * i) % k);
    }
} */