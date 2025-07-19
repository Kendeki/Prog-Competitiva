/*
  Implementação recursiva da busca binária, como passado de exercício na aula 3.
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll _search(
  vector<ll> v,
  ll x,
  ll l,
  ll r
)
{
  if (l == r)
    if (l < v.size() and v[l] >= x) return l;
    else return -1;
  
  ll mid = (l+r)>>1;
  
  if (v[mid] >= x)
    return _search(v, x, l, mid);
  else
    return _search(v, x, mid+1, r);
}

ll search(vector<ll> v, ll x)
{
  return _search(v, x, 0, v.size());
}
