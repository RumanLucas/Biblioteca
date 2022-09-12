import numpy as np
import matplotlib.pyplot as plot
from typing import List

def main():
  lista = [1,2,3]

  U = cria_vetor3(lista)
  
  print("lista", lista)
  
  print("vetor por linha:")
  print(U)
  print("tamanho do vetor",np.shape(U))

def checa_vetor3(v: np.array)->None:
  if v.shape != (3,1):
    raise ValueError('A lista deveria ter 3 posiçoes')
    exit(main.py)


def cria_vetor3(vlist: list)->np.array:
  if len(vlist)==3:
    res = np.zeros([3,1])
    for c1 in range(0,len(vlist)):
      res[c1,0] = vlist[c1]
    return res
  checa_vetor3(vlist)

main()