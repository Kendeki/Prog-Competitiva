// https://codeforces.com/problemset/problem/742/A

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define IN(dest) cin >> dest;
#define ANS(x) cout << (x) << '\n';

int main()
{
  ll n; IN(n);
  ll a[4] = {8,4,2,6}; // 8^1, 8^2, 8^3, ...
  ANS(n == 0 ? 1 : a[--n%4]);
}
