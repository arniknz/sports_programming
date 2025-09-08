# ROUND: https://codeforces.com/contest/1742


# A
"""for _ in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] == a[2]:
        print('YES')
    else:
        print('NO')"""


# B
"""for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    f = False
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            f = True
            break
    if f:
        print('NO')
    else:
        print('YES')"""


# C
"""for _ in range(int(input())):
    input()
    f = False
    mt = [input() for _ in range(8)]
    for row in mt:
        if row.count('R') == 8:
            f = True
            break
    if f:
        print('R')
    else:
        print('B')"""


# D
"""cpp

#include <bits/stdc++.h>

using namespace std;

#define f(n) for (int i = 0; i < n; i++)

int my_gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return my_gcd(b, a % b);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n), v(1001, -1);
        f(n) cin >> a[i];
        f(n) v[a[i]] = i;

        auto mx = -1;
        for (int i = 0; i < 1001; i++) {
            if (v[i] != -1) {
                for (int j = i; j < 1001; j++) {
                    if (v[j] != -1) {
                        if ((my_gcd(i, j) == 1)) {
                            mx = max(mx, v[i] + v[j] + 2);
                        }
                    }
                }
            }
        }
        cout << mx << endl;
    }

    return 0;
}
"""


# E
"""for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))
    cnts = []
    for i in range(q):
        cnt = 0
        for j in range(n):
            if k[i] >= a[j]:
                cnt += a[j]
            else:
                break
        cnts.append(cnt)
    print(*cnts)"""
# TL

def calculate_prefix_sum(arr):
    if not arr:
        return []

    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    return prefix_sum


for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))
    p = calculate_prefix_sum(a)
    cnt = []
    for i in range(q):
        l, r = 0, n - 1
        mx = []
        while l < r:
            mid = (l + r + 1) // 2
            if p[mid] >= k[i]:
                mx.append(mid)
                r = mid - 1
            else:
                l = mid + 1
    print(cnt)
