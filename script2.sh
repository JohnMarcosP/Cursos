#!/bin/bash
echo "Qual a sua nota da prova?"
read nota

if [ "$nota" -gt 70 ]
then
echo "aprovado"
else
echo "reprovado"
fi
