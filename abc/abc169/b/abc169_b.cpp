#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using P = pair<int, int>;
using Pll = pair<ll, ll>;

const static int MOD = 1e9 + 7;
const int MAX = 1e9;
const ll LLMAX = 1e18;
const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const double PI = acos(-1.0);

#define DEBUG(x) cerr << #x << ": " << x << endl;
#define DEBUG_VEC(v)                   \
    cerr << #v << ":";                 \
    for (int i = 0; i < v.size(); i++) \
        cerr << " " << v[i];           \
    cerr << endl;
#define DEBUG_MAT(v)                            \
    cerr << #v << endl;                         \
    for (int i = 0; i < v.size(); i++) {        \
        for (int j = 0; j < v[i].size(); j++) { \
            cerr << v[i][j] << " ";             \
        }                                       \
        cerr << endl;                           \
    }

#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, n) for (int i = 1; i <= (n); ++i)
#define REP(i, a, n) for (int i = a; i <= (n); ++i)

int main() {
    int N; cin >> N;
    vector<ll> A(N); rep(i, N) cin >> A[i];
    sort(A.begin(), A.end());
    // DEBUG_VEC(A)

    if (A[0] == 0) {
        cout << 0 << endl;
        return 0;
    }

    ll ans = 1;
    rep(i, N) {
        if (ans > LLMAX / A[i]) {
            cout << -1 << endl;
            return 0;
        }
        ans *= A[i];
    }

    cout << ans << endl;

    return 0;
}
