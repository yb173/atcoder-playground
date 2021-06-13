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

#define rep(i, n) for (int i = 0; i < (n); ++i)
#define rep1(i, n) for (int i = 1; i <= (n); ++i)
#define REP(i, a, n) for (int i = a; i <= (n); ++i)

#define DEBUG(x) cerr << #x << ": " << x << endl;
#define DEBUG_VEC(v)\
    cerr << #v << ":";\
        for (int i = 0; i < v.size(); i++)\
        cerr << " " << v[i];\
    cerr << endl;
#define DEBUG_MAT(v)\
    cerr << #v << endl;\
    for (int i = 0; i < v.size(); i++) {\
        for (int j = 0; j < v[i].size(); j++) {\
            cerr << v[i][j] << " ";\
        }\
    cerr << endl;\
    }

int main() {
    int N, M; cin >> N >> M;
    vector<vector<int>> G(N);

    rep(i, M) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        G[a].push_back(b);
    }

    int ans = 0;
    rep(sv, N) {
        queue<int> q;
        vector<bool> used(N, false);
        used[sv] = true;
        q.push(sv);
        while (q.size()) {
            int v = q.front(); q.pop();
            for (int u : G[v]) {
                if (used[u]) continue;
                used[u] = true;
                q.push(u);
            }
        }
        rep(i, N) if (used[i]) ans++;
    }

    cout << ans << endl;
    return 0;
}
