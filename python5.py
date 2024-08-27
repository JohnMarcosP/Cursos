#!/usr/bin/python3
import sys

def soma(numero1,numero2):
  return numero1+numero2

def divisao(numero1,numero2):
    return numero1/numero2
if len(sys.argv) >=3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[2] !="0":
        primeiro_numero = int(sys.argv[1])
        segundo_numero = int(sys.argv[2])
        print("A soma do primeiro numero com o segundo eh:", soma(primeiro_numero,segundo_numero))
        print("A divisao do primeiro numero com o segundo eh:", divisao(primeiro_numeor,segundo_numero))
    else:
      print("Os valores precisam ser numericos")
else:
  print("Deve-se passar dois numeros como parametros")
