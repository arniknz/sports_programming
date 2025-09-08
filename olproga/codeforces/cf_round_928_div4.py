# ROUND: http://codeforces.com/contest/1926


# A
"""for _ in range(int(input())):
    s = list(input())
    cnta = 0
    cntb = 0
    for i in range(len(s)):
        if s[i] == 'A':
            cnta += 1
        else:
            cntb += 1
    if cnta > cntb:
        print('A')
    else:
        print('B')"""


# B
"""for _ in range(int(input())):
    res = []
    n = int(input())
    for _ in range(n):
        row = list(map(int, input().split()))
        res.append(sum(row))
    
    res = sorted(res, reverse=True)
    if res[0] == res[1]:
        print("SQUARE")
    else:
        print("TRIANGLE")"""


# C
"""#include <iostream>

using namespace std;

const int MAX = 200001;

int s[MAX];

int sum_of_digits(int x) {
    int res = 0;
    while (x) {
        res += x % 10;
        x /= 10;
    }

    return res;
}

void print() {
    int x;
    cin >> x;
    cout << s[x] << '\n';
}

int main()
{
    int t;
    cin >> t;

    s[0] = 0;
    for (int i = 1; i < MAX; i++) {
        s[i] = s[i - 1] + sum_of_digits(i);
    }

    for (int i = 1; i <= t; i++) {
        print();
    }
}"""


# D
