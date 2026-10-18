from colorama import init, Fore, Style

# Inicializa o Colorama
init()

# Lista com as situações dos níveis do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]


def definir_cor(nivel):
    """
    Define a cor da mensagem conforme o nível informado.
    """

    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }

    return cores.get(nivel, Fore.WHITE)


def exibir_nivel(nivel):
    """
    Exibe a situação do reservatório com a cor correspondente.
    """

    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print("\nSituação atual do reservatório:")
    print(cor + mensagem + Style.RESET_ALL)


# Entrada de dados
while True:
    try:
        nivel_atual = int(
            input("Digite o nível atual do reservatório, de 1 a 5: ")
        )

        if nivel_atual in range(1, 6):
            break

        print("Digite um nível válido entre 1 e 5.")

    except ValueError:
        print("Digite apenas números inteiros.")


# Exibe o resultado
exibir_nivel(nivel_atual)
