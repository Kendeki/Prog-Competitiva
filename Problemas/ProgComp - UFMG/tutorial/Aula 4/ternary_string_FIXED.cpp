#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;
#define endl '\n'

#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';
#define FOR(I, n) for(;I<n;I++)

void solve()
{
	string v; IN(v);
	ll N = v.size();
	ll msize = 200010;
	ll l = 0, r = 0;
	vll c(3,0);
#define PUT(X) c[v[X] - '1']++
#define POP(X) c[v[X] - '1']--
#define CHK c[0] and c[1] and c[2]
	FOR(l, N)
	{
		FOR(r, N)
		{
			if (CHK) break;
			PUT(r);
		}
		if (CHK) msize=min(msize, r-l);
		POP(l);
	}
	if (msize == 200010) ANS(0)
	else ANS(msize);
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  cout.tie(nullptr);

#ifndef SINGLE
    ll t; cin >> t;
    while(t--)solve();
#else
	solve();
#endif
}
