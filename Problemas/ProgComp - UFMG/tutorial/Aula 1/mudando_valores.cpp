#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

typedef long long ll;

void solve()
{
  ll n, c, i; cin >> n;
  vector<ll> v;
  priority_queue<ll> pq;
  map<ll, ll> m;
  
  for (i = 0; i < n; i++)
  {
    cin >> c;
    v.push_back(c);
    pq.push(-c);
  }
  
  for (i = 0; !pq.empty(); pq.pop(), i++)
  {
    c = -pq.top();
    m[c] = i;
  }
  
  for (auto c : v)
    cout << m[c] << " ";
    
  cout << endl;
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
