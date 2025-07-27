#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';
#define FOR(I, n) for(ll I=0;I<n;I++)

void solve()
{
	cout << fixed << setprecision(10);
	double N; IN(N);
	double l = 0, r = 1e8+10; // limite: 1 < N < 10^16, logo, raiz max = 10^8 ou 1e8
	FOR(i, 200) // numero fixo de iterações
	{
		double m = (l+r)/2;
		if (m*m > N) r = m;
		else l = m;
	}
	ANS((l+r)/2);
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
