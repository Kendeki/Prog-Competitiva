// https://codeforces.com/problemset/problem/2114/B

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() 
{
  ios_base::sync_with_stdio(0);
  cin.tie(nullptr);
  cout.tie(nullptr);
  
  char c;
  ll t, n, i, o, z, k, zp, op, tp;
  cin >> t;
  
  while (t --> 0)
  {
    cin >> i >> k;
    n = i;
    o = 0;
    z = 0;
    zp = 0;
    op = 0;
    if (n % 2 != 0) o = z = 1;
    while (i --> 0)
    {
      cin >> c;
      if (c == '1') o++;
      else z++;
    }
    op = o / 2;
    zp = z / 2;
    tp = 0;
    while (op > 0 or zp > 0)
    {
      if (tp < k)
      {
        if (op > zp) op--;
        else zp--;
        tp++;
      }
      else
      {
        op--;
        zp--;
        if (op < 0 or zp < 0)
        {
          if (op > zp) zp++;
          else op++;
          tp++;
        }
      }
    }
    if (tp == k and op - zp == 0)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}
