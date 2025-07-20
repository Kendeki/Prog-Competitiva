// https://codeforces.com/problemset/problem/1374/C

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';
#define FOR(I, n) for(ll I=0;I<n;I++)

void solve()
{
  ll n; cin >> n;
  char c;
  ll ans = 0;
  ll count = 0;
  FOR(i, n)
  {
    IN(c);
    if (c == '(') count++;
    else
    {
      if (count < 1) ans++;
      else count--;
    }
  }
  ANS(ans);
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  cout.tie(nullptr);
  
#define SINGLE false

  if (!SINGLE)
  {
    ll t; cin >> t;
    while(t--)solve();
  } else solve();
}
