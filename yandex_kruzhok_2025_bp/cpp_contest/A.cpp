/* #include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    stack<int> st;
    while (n--) {
        int x;
        cin >> x;
        st.push(x);
    }
    stack<int> ans;
    while (!st.empty()) {
        int tmp = st.top();
        st.pop();
        while (!ans.empty() && ans.top() < tmp) {
            st.push(ans.top());
            ans.pop();
        }
        ans.push(tmp);
    }
    while (!ans.empty()) {
        int x = ans.top();
        cout << x << " ";
        ans.pop();
    }
    cout << endl;
    return 0;
}*/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    queue<int> st;
    stack<int> p;
    vector<pair<int, int>> ans;
    int i = 1;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        st.push(x);
    }
    while (i <= n) {
        if (!p.empty() && p.top() == i) {
            int cnt = 0;
            while (!p.empty() && p.top() == i) {
                cnt++;
                i++;
                p.pop();
            }
            ans.push_back({2, cnt});
        } else if (!st.empty()) {
            int x = st.front();
            p.push(x);
            st.pop();
            ans.push_back({1, 1});
        } else {
            cout << 0 << endl;
            return 0;
        }
    }
    cout << ans.size() << endl;
    for (auto x : ans) {
        cout << x.first << " " << x.second << endl;
    }
    return 0;
}