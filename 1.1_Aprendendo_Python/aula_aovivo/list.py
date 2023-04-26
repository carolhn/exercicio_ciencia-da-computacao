names_list = ['Duda', 'Rafa', 'Cris', 'Yuri']
new_names_list = [name for name in names_list if 'a' in name]

# Aqui o for percorre cada nome em "names_list", verifica
# se existe a letra "a" nele,
# o adiciona à variável "name", e então gera nossa nova lista "new_names_list"
print(new_names_list)

# Saída
['Duda', 'Rafa']


quadrados = [x*x for x in range(11)]
print(quadrados)

# Saída
# Isto é equivalente às operações de map e filter em JavaScript.
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
