AGENDA = {
  "Guilherme": {
    "Telefone" : "99852-9526",
    "email" : " GuiZe@gmail.com",
    "endereco": "Avenida Cruvnial"
  },
  "Maria":{
    "Telefone" : "98456-6135",
    "email" : "Maria@gmail.com",
    "endereco": "av.Flores"
  },
  "Joao": {
    "Telefone" : "9999-4118",
    "email" : "joao@gmail.com",
    "endereco" : "Rua das Rosas"
  },
}

AGENDA['Guilherme']['endereco'] = "Rua das nacoes"
#print(AGENDA['Guilherme']['endereco'])
AGENDA['Lucas'] = {
  "Telefone" : "98496-4686",
  "email":"lucasca@gmail.com",
  "endereco": "rua dos pavoes"
},

for contato in AGENDA:
  print(contato)
print(AGENDA['Lucas'])
