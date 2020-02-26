

def get_max_attempts():
    while True:
        max_attempts = input("Informe o número máximo de tentativas para chutar as letras: ")
        try:
            max_attempts = int(max_attempts)
            return max_attempts
        except:
            print("O valor digitado não é um número inteiro. Tente novamente.")

def get_min_length():
    while True:
        min_lenght = input("Informe o tamanho mínimo da palavra para o jogo: ")
        try:
            min_lenght = int(min_lenght)
            return min_lenght
        except:
            print("O valor digitado não é um número inteiro. Tente novamente.")

def get_next_letter():
    while True:
        next_letter = input("Digite a próxima letra: ").lower()
        if len(next_letter) != 1:
            print("Você digitou mais de uma letra, digite novamente.")
        else:
            return next_letter
