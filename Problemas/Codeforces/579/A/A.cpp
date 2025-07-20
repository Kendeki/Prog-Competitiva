#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';

int main()
{
  ll x; IN(x);
  ANS(__builtin_popcount(x));
}
