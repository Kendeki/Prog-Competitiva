// https://codeforces.com/problemset/problem/1690/C

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  cout.tie(nullptr);
  
  ll t, n, d, s, f, l, c;
  cin >> t;
  
  pair<ll,ll> s_f;
  
  while (t --> 0)
  {
    cin >> n;
    
    queue<ll> q;
    
    while (n --> 0)
    {
      cin >> c;
      q.push(c);
    }
    
    queue<pair<ll,ll>> p;
    
    while (!q.empty())
    {
      s = q.front(); q.pop();
      cin >> f;
      p.push(make_pair(s, f));
    }
    
    d = 0;
    l = -1;
    
    while (!p.empty())
    {
      s_f = p.front(); p.pop();
      s = s_f.first;
      f = s_f.second;
      
      if (s < l)
      {
        s = l;
      }
      
      cout << f - s << " ";
      
      l = f;
    }
    cout << endl;
  }
}
