// https://codeforces.com/problemset/problem/1932/A

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
  char c, l;
  ll t, n, i;
  cin >> t;
  
  while (t --> 0)
  {
    cin >> n;
    l = -1;
    i = 0;
    
    while (n --> 0)
    {
      cin >> c;
      if (l == '*' and c == l)
      {
        while (n --> 0) cin >> c;
        break;
      }
      if (c == '@') i++;
      l = c;
    }
    
    cout << i << endl;
  }
}
