#!/usr/bin/python3
import sys
if len(sys.argv) >=3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[2] != "0":
      primeiro_numero = int(sys.argv[1])
      segundo_numero = int(sys.argv[2])
      print("A soma do primeiro numero com o segundo eh:", primeiro_numero+segundo_numero)
      print("A divisao do primeiro numero com o segundo eh:", primeiro_numero/segundo_numero)
    else:
      print("Os valores precisam ser numericos")
else:
    print("Passar dois numeros como argumento")
