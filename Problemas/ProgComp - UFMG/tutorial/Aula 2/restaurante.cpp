#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

typedef long long ll;

#define START first
#define END second

bool comp(pair<ll, ll> a, pair<ll, ll> b)
{
  return a.END < b.END;
}

void solve()
{
  ll n, s, e, ans, l; cin >> n;
  vector<pair<ll, ll>> v;
  
  while (n--)
  {
    cin >> s >> e;
    v.emplace_back(s, e);
  }

  sort(v.begin(), v.end(), comp);
  
  ans = 0;
  l = -1;
  for (auto p : v)
  {
    if (p.START > l)
    {
      l = p.END;
      ans++;
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
