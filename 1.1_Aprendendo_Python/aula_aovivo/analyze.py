def analyze(text):
    report = ""

    count = len(text.split(" "))
    report += f"Numero de palavras = {count}/n"

    char_count = dict()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    report += f"Numero de palavras = {char_count}"
    return report


text_to_analyze = {
    "seremos a primeira geração a deixar o mundo pior do que encontramos"
    "a gente não quer só comida, a gente quer comida, diversão e arte"
}

print(analyze(text_to_analyze))
