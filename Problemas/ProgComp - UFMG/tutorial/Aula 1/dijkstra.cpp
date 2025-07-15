#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

typedef long long ll;

void solve()
{
  unordered_set<string> s;
  string l;
  while (getline(cin, l))
  {
    s.insert(l);
  }
  cout << s.size() << endl;
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
