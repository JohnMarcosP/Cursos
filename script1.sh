#!/bin/bash

echo "Digite r para rotas ou i para Interfaces de Rede: "
read entrada
if [ "$entrada" == "r" ]
then
echo "Mostrando rotas:"
route -n
elif [ "$entrada" == "i" ]
then
echo "Digite uma interface de rede:"
read interface
echo "Mostrando informacoes da interface de rede $interface"
ifconfig $interface
else
echo "Opcao invalida"
fi
