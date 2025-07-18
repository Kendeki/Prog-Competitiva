#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define endl '\n'

void solve()
{
  ll n; cin >> n;
  ll c, prev, ans;
  cin >> prev; n--;
  ans = prev;
  while (n--)
  {
    cin >> c;
    if (c > (c + prev)) prev = c;
    else prev += c;
    
    ans = max(prev, ans);
  }
  cout << ans << endl;
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
