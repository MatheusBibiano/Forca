"""
    JOGO DA FORCA

    ---------
    |       !    
    |       o
    |      /|\         _ _ _ _ _
    |      / \  
    |   
  -----  

  FEITO POR: Matheus Bibiano Alves
  DATA: 07/06/2021
"""

from os import system
from sys import platform


def clear():
    """
    Limpa a tela do terminal.
    """
    if platform == "linux" or platform == "linux2":
        system("clear")

    elif platform == "darwin":
        system("clear")

    elif platform == "win32":
        system("cls")


def pause():
    """
    Pause a execução do programa.
    """
    if platform == "linux" or platform == "linux2":
        system("echo Enter para continuar...")
        system("read enter")

    elif platform == "darwin":
        system("echo Enter para continuar...")
        system("read enter")

    elif platform == "win32":
        system("pause")


def find(letter: str, array: str, indexes):
    """
        Busca uma letra dentro de uma lista, caso a encontre retorna uma lista com os indices.
    """
    index = array.find(letter)
    
    if index != -1:
        indexes.append(index)
        array = list(array)
        array[index] = '-'
        array = ''.join(array)

        if len(array) > 0:
            return find(letter, array, indexes)
        
        else:
            return indexes
    
    else:
        if len(indexes) > 0:
            return indexes

        else:
            return False
        

def handleInput(input: str):
    """
        Faz o tratamento da entrar do usuário.
    """
    input = input.strip()
    input = input.upper()

    if input.isalpha():
        return input

    else:
        return -1


def main():
    word = str(input("\nPALAVRA SECRETA: "))
    clear()
    
    while len(word) < 2:
        print("[!] INSIRA UMA PALAVRA!")
        word = str(input("PALAVRA SECRETA: "))
        clear()

    word = handleInput(word)

    if word != -1:
        lifes = 7
        size_secret_word = len(word)
        discover_word = list("_" * size_secret_word)
        typed_letters = []
        count_hit = 0
        lose = False
        win = False

        while not lose and not win:
            if lifes > 0:
                print(f"VIDAS: {lifes}")
                print(f"PALAVRA SECRETA: {discover_word}")
                print(f"LETRAS UTILIZADAS: {typed_letters}")

                attempt = str(input("\nESCOLHA UMA LETRA >> "))

                while len(attempt) != 1:
                    print("[!] APENAS UMA LETRA!")
                    attempt = str(input("\nESCOLHA UMA LETRA >> "))

                attempt = handleInput(attempt)

                if attempt != -1:
                    if attempt in typed_letters:
                        lifes -= 1
                        print("JÁ FOI UTILIZADA!")
                        pause()
                        clear()
                    
                    else:
                        indexes_found = find(attempt, word, [])

                        if indexes_found is not False:
                            count_hit += 1

                            for i in indexes_found:
                                discover_word[i] = word[i]
                                
                            print("ACERTOU!")

                            check_word = ''.join(discover_word)

                            if check_word.isalpha():
                                win = True
                                pause()
                                clear()
                                print("PARABÊNS! VOCÊ GANHOU!")

                            pause()
                            clear()
                            
                        else:
                            lifes -= 1
                            print("ERROU!")
                            pause()
                            clear()

                        typed_letters.append(attempt)

                else:
                    print("[!] SUA ENTRADA NÃO SEGUE OS CRITÉRIOS!")
                    pause()
                    clear()

            else:
                lose = True
                print("VOCÊ PERDEU!")
                pause()
                clear()

    else:
        print("[!] SUA ENTRADA NÃO SEGUE OS CRITÉRIOS!")


if __name__ == '__main__':
    main()
