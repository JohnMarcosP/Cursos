#!/usr/bin/python3
# Inteiros
# Strings
# Float
primeiro_numero = int(input("Digite o primeiro numero:"))
segundo_numero = int(input("Digite o segundo numero:"))
print("Digite se voce quer realizar uma soma ou uma divisao")
entrada = input()
if entrada == "soma":
    print("A soma do primeiro numero com o segundo eh: ", primeiro_numero+segundo_numero)
elif entrada == "divisao":
    print("A divisao do primeiro numero com o segundo eh:", primeiro_numero/segundo_numero)
