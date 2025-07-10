// https://codeforces.com/problemset/problem/1714/B

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
  ll t, n, c, i;
  cin >> t;
  
  while (t --> 0)
  {
    cin >> i;
    n = i;
    
    stack<ll> s;
    map<ll, bool> added;
    
    while (i --> 0)
    {
      cin >> c;
      s.push(c);
    }
    
    while (!s.empty())
    {
      c = s.top();
      s.pop();
      
      if (added.find(c) != added.end())
      {
        cout << n << endl;
        goto next;
      }
      
      n--;
      
      added.insert({c, true});
    }
    
    cout << 0 << endl;
    
    next:;
  }
}
