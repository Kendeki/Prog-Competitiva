// Exemplo de função que calcula fatorial de N

ll fac(ll N)
{
  vector<int> fat(N+1);
  fat[0] = 1;
  for (i = 0; i < 11; i++) fat[i] = fat[i-1]*i;
  return fat[N];
}
