#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;
#define endl '\n'

#define VAL(x) cout << #x << ": " << x << '\n';
#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';
#define FOR(I, n) for(ll I=0;I<n;I++)

void solve()
{
	ll n, c, t; cin >> n >> c >> t;
	ll l=0, r=100000007, mid;
	vll p(n); FOR(i, n) IN(p[i]);
	auto possible = [=](ll test)
	{
		ll C = c;
		ll T = t * test;
		FOR(i, n)
		{
			if (p[i] > T) { i--; C--; T = t * test; }
			else T = T - p[i];
			if (C <= 0) return false;
		}
		return true;
	};
	while (l < r)
	{
		mid = (l+r)/2;
		if (!possible(mid))
			l = mid + 1;
		else
			r = mid;
	}
	ANS(l);
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  cout.tie(nullptr);
  
#define SINGLE true

  if (!SINGLE)
  {
    ll t; cin >> t;
    while(t--)solve();
  } else solve();
}
