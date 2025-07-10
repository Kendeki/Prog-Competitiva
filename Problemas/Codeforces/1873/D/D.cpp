// https://codeforces.com/problemset/problem/1873/D

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
  char c;
  ll t, n, k, i, j, kk, o;
  cin >> t;
  
  while (t --> 0)
  {
    cin >> i >> k;
    n = i;
    vector<bool> s;
    
    while (i --> 0)
    {
      cin >> c;
      s.push_back(c == 'W');
    }
    
    i = 0;
    o = 0;
    
    while (i < n)
    {
      j = i;
      
      kk = k;
      if (s[i]) {
        i++;
        continue;
      }
      while (
        j < n and
        kk --> 0
      )
        j++;
      o++;
      i = j;
    }
    cout << o << endl;
  }
}
