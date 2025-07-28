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
	ll N, X; IN(N); IN(X);
	vll v(N); FOR(i, N) IN(v[i]);
	ll i=0, j=N-1;
	while (i < j)
	{
		if   (v[i] + v[j] == X) goto yes;
		if   (v[i] + v[j]  > X) j--;
		else                    i++;
	}
	ANS("NO");
	return;
yes:
	ANS("YES");
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  cout.tie(nullptr);

#define SINGLE

#ifndef SINGLE
    ll t; cin >> t;
    while(t--)solve();
#else
	solve();
#endif
}
