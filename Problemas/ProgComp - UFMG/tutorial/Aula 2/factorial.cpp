#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

typedef long long ll;

void solve()
{
  ll n, i, ans; cin >> n;
  vector<int> fat(11);
  fat[0] = 1;
  for (i = 1; i < 11; i++) fat[i] = fat[i-1]*i;
  i = 10;
  ans = 0;
  while (n > 0)
  {
    ll f = fat[i];
    if (f > n)
      i--;
    else
    {
      ans++;
      n -= f;
    }
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
  
  return 0;
}
