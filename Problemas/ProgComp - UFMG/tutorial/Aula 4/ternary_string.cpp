#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;
#define endl '\n'

#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';
#define FOR(I, n) for(ll I=0;I<n;I++)

void solve()
{
	string v; IN(v);
	ll N = v.size();
	ll S = N;
	ll l = 0, r = N-1;
	vll c(3,0);
#define PUT(X) c[v[X] - '1']++
#define POP(X) c[v[X] - '1']--
#define ASK(X) c[v[X] - '1']>0 // TIL -1 is true. Of course it is
	FOR(i, N) PUT(i);
	if (c[0] and c[1] and c[2])
	{
		l=0;r=N-1;
		while(l < r and (ASK(l) or ASK(r)))
		{
			POP(l); if (ASK(l)) l++;
			POP(r); if (ASK(r)) r--;
		}
		ANS((r-l)+1);
	}
	else
		ANS(0);
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
