import json

pessoa ={
  "nome": "Eduardo Felipe",
  "sobrenome": "Costa",
  "enderecos": [
    {
      "rua": "R1",
      "numero": 32
    },
    {
      "rua": "R2",
      "numero": 55
    }
  ],
  "altura": 1.7,
  "numeros_preferidos": [
    2,
    4,
    6,
    8,
    10
  ],
 
}
with open('aula190_a.json','w',encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2, ensure_ascii = False)
