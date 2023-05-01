# leitura de arquivos
# open - faz a leitura dos arquivos (dois
# para 1 - nome do arquivo que quero ler 2 - modo como eu quero interagir)
characteres_file = open("meus-personagens-favoritos.txt", mode='w')

# escrever arquivo
characteres_file.write("Goku\n")
characteres_file.write("Vegeta\n")
characteres_file.write("Gohan\n")
characteres_file.write("Piccolo\n")

#  output vai jogar no arquivo
print('batmam', file=characteres_file)

# -----
more_characteres = ['Bulma', 'Kuririn', 'Yamcha', 'Trunks', 'Goten', 'Chichi']
# escrever uma lista
characteres_file.writelines(more_characteres)

# fechar o arquivo
characteres_file.close()
