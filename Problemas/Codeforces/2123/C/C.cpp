// https://codeforces.com/problemset/problem/2123/C

#include <bits/stdc++.h>

using namespace std;

#define INF 1ll<<60

typedef long long ll;

void solve()
{
    ll n, i;
    cin >> n;
    vector<ll> a(n + 1), pre(n + 2, INF), suf(n + 2, 0);
    
    for (i = 1; i <= n; i++)
    {
        cin >> a[i];
        pre[i] = min(pre[i - 1], a[i]);
    }
    
    for (i = n; i >= 1; i--)
    {
        suf[i] = max(suf[i + 1], a[i]);
    }
    
    for (i = 1; i <= n; i++)
    {
        if (a[i] == pre[i] or a[i] == suf[i])
            cout << 1;
        else
            cout << 0;
    }
    cout << endl;
}

int main()
{
    ll t;
    cin >> t;
    while (t--) solve();
}

