#include <bits/stdc++.h>
// #include<iostream>
// #include<algorithm>
// #include<math.h>
// #include<vector>
// #include<map>
// #include<set>
// #include<iomanip>

using namespace std;
using ll = long long;
using P = pair<int, int>;

const int MOD = 1e9 + 7;
const int MAX = 1e9;
const ll LLMAX = 1e18;
const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const double PI = acos(-1.0);

#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rrep(i, a, n) for (int i = a; i <= (n); ++i)

int main() {
    int N, K; cin >> N >> K;

    vector< pair<ll, int> > ab;
    rep(i, N) {
        ll a;
        int b;
        cin >> a >>  b;
        pair<ll, int> p(a, b);
        ab.push_back(p);
    }

    rep(i, N) {
        cout << ab[i].first << ab[i].second << endl;
    }

    return 0;
}
