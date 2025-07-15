#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

typedef long long ll;

void solve()
{
  char c;
  ll n, sz, p;
  cin >> n;
  
  vector<pair<ll, ll>> tamanho(61, pair<ll,ll>(0, 0));
  
  p = 0;
  
  while (n--)
  {
    cin >> sz >> c;
    
    ll D, E;
    D = tamanho[sz].first;
    E = tamanho[sz].second;
    
    tamanho[sz] = make_pair(
      c == 'D' ? ++D : D,
      c == 'E' ? ++E : E
    );
    
    if (D and E)
    {
      p++;
      tamanho[sz] = make_pair(--D, --E);
    }
  }
  
  cout << p << endl;
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
