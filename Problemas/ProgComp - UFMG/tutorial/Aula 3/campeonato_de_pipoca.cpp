#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vll;

#define IN(dest) cin >> dest;
#define ANS(x) cout << x << '\n';
#define FOR(I, n) for(ll I=0;I<n;I++)

void solve()
{
  ll N, C, T;
  cin >> N >> C >> T;
  
  vll pi(N);
  
  FOR(i, N) IN(pi[i]);
  
  auto possible = [=](ll test)
  {
    ll n = T*test; // pipocas max. durante todo o tempo teste.
    ll c = C;
    FOR(i, N)
    {
      auto p = pi[i];
      if (n >= p) n -= p;
      else
      {
        n = T*test;
        c--;
        // volta um índice, pois cada saco
        // de pipoca só pode ser comido
        // por um competidor, então, precisamos
        // repetir o elemento atual.
        i--;
      }
      // encerra o loop caso seja impossivel prosseguir.
      if (c <= 0) return false;
    }
    return true;
  };
  
  ll l = 0, r = 1e9+1;

  // Usando a busca binária para filtrar a resposta mínima.
  // O(n * log n). O(log n) na busca e O(n) no algoritmo guloso
  // de checagem de resposta.
  while (l < r)
  {
    ll mid = (l+r)/2;
    if (!possible(mid))
      l = mid + 1;
    else
      r = mid;
  }

  ANS(l);
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
}
