# Funções úteis para input em python

"""
Versões curtas das funções:
  receber_n_inteiros:
    [int(x) for x in input().split()]
  receber_linhas:
    import sys; sys.stdin.readlines()
  receber_linhas (com aplicação de função extra):
    import sys; [
      ... # corpo da função
      for line in sys.stdin.readlines()
    ]
  receber_linhas_com_n_inteiros:
    import sys; [
      [int(x) for x in line.split()]
      for line in sys.stdin.readlines()
    ]
"""

import sys

def receber_n_inteiros(n = None, entrada = input, separador = " "):
  if callable(entrada):
    entrada = entrada()
  sep = entrada.split(separador)
  if n is not None: assert len(sep) == n
  return [int(x) for x in sep]

def receber_linhas(aplicar = None):
  if callable(aplicar):
    return [
      aplicar(linha) for linha in sys.stdin.readlines()
    ]
  return sys.stdin.readlines()

def receber_linhas_com_n_inteiros(*args, **kwargs):
  return receber_linhas(
    aplicar = lambda l:
      receber_n_inteiros(*args, entrada = l, **kwargs)
  )
