while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Se nenhuma exceção ocorrer, a cláusula except é ignorada
# e a execução da instrução try é finalizada.


# Sempre devemos fechar um arquivo e podemos, em um bloco try,
#  fazer isso utilizando a instrução finally ou else.
#  A instrução finally é sempre executada antes de sair da cláusula try.
#  A instrução else é executada se e somente se nenhuma exceção for lançada.
#  A i finally é executada independentemente d 1 exceção ter sido ou n lançada.
