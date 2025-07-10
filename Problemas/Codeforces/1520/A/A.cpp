// https://codeforces.com/problemset/problem/1520/A

#include <bits/stdc++.h>
using namespace std;

int main()
{
  char task, last;
  int t, n, i;
  cin >> t;
  
  while (t --> 0)
  {
    bool started[26] = {false};
    
    cin >> n;
    
    last = -1;
    
    while (n --> 0)
    {
      cin >> task;
      
      i = task - 'A';
      
      if (started[i] and last != task)
      {
        cout << "NO" << endl;
        while (n-->0) cin>>task;
        goto next;
      }
      
      last = task;
      
      started[i] = true;
    }
    
    cout << "YES" << endl;
    
    next:
  }
}
