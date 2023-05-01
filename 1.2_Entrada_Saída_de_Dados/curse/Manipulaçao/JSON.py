import json

# aqui retorna todo o arquivo json
with open('nome_do_arquivo.json') as super_herois:
    print(json.load(super_herois)[0])

# aqui tem poder de pegar por algum parametro especifico(nome)
with open('nome_do_arquivo.json') as super_herois:
    list = json.load(super_herois)
    for item in list:
        print(item['name'])
