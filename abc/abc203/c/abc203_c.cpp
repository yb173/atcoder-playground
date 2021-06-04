#include <bits/stdc++.h>

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
    int N; cin >> N ;
    ll K; cin >> K;

    vector<pair<ll, int>> ab(N);
    rep(i, N) {
        cin >> ab[i].first >> ab[i].second;
    }
    sort(ab.begin(), ab.end());

    ll pos = K;
    rep(i, N) {
        if (ab[i].first > pos) break;
        pos += ab[i].second;
    }

    cout << pos << endl;

    return 0;
}

// 参考
// https://atcoder.jp/contests/abc203/submissions/23037667
