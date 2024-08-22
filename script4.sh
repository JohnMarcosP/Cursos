#!/bin/bash

if [ "$1" == "r" ]
then
echo "Mostrando rotas"
route -n
elif [ "$1" == "i" ]
then
echo "Mostrando informacoes da interface de rede $2"
ifconfig $2
else 
echo "Usage: ./script4.sh r|i eth0"
fi
