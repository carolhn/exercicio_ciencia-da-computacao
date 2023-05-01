import csv

# aqui retorna todo o arquivo json
with open('arquivo.csv') as super_herois:
    print(csv.DictReader(super_herois))

# aqui tem poder de pegar todos os parametros do objeto
with open('nome_do_arquivo.json') as super_herois:
    list = csv.DictReader(super_herois)
    for item in list:
        print(item)

# conseguimos fazer a mesa coisa com o csv.reader
with open('nome_do_arquivo.json') as super_herois:
    header, *data = csv.reader(super_herois)
    print(data)
