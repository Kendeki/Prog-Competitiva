#include <bits/stdc++.h>
using namespace std;

#define _ ios_base::sync_with_stdio(0); cin.tie(nullptr);

typedef long long ll;
typedef vector<ll> vl;

#define INF (1ll<<60)

#define endl '\n'

int main()
{ _
  ll n, c, i, j, ans;
  ll t; cin >> t;
  while (t --> 0)
  {
    cin >> i;
    n = i;
    vl v;
    while (i --> 0)
    {
      cin >> c;
      v.push_back(c);
    }
    
    i = 0;
    ans = INF;
    while (i < n)
    {
      j = i;
      while (j < n and v[i] == v[j])
        j++;
      ans = min(ans, (i + n - j)*v[i]);
      i = j;
    }
    cout << ans << endl;
  }
}
