from get_words import get_word
from get_parameters import get_max_attempts, get_min_length, get_next_letter


def game():
    max_attempts = get_max_attempts()
    min_length = get_min_length()
    word = get_word(min_length)
    correct_words = []
    past_letters = []
    attempts = 0
    

    while True:
        word_to_show = ""
        for letter in word:
            word_to_show += letter if letter in correct_words else "*"

        print("PALAVRA: ", word_to_show)
        print("QUANTIDADE DE LETRAS:", len(word))
        print("LETRAS CHUTADAS:", past_letters)
        print("TENTATIVAS RESTANTES:", max_attempts-attempts)
        if not "*" in word_to_show and attempts < max_attempts:
            print("VOCÊ VENCEU!")
            return word_to_show
        elif "*" in word_to_show and attempts >= max_attempts:
            print("VOCÊ PERDEU! :(")
            print("Vocêr atingiu o número máximo de tentativas e não conseguiu descobrir a palavra.")
            return word_to_show
            
        next_letter = get_next_letter()
        attempts += 1
        if next_letter in past_letters or next_letter in correct_words:
            print("Você já chutou essa letra, tente outra! (essa tentativa não será descontada das suas tentativas restantes)")
            attempts -= 1
        if next_letter in word:
            print(f"Boa! Tem a letra *{next_letter}* na palavra! :)")
            if next_letter not in correct_words:
                correct_words.append(next_letter)
        else:
            print(f"Poxa, não tem a letra *{next_letter}* na palavra! :(")
            if next_letter not in past_letters:
                past_letters.append(next_letter)
        
        
        

if __name__ == "__main__":
    game()

