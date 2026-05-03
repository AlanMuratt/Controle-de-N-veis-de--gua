from colorama import init, Fore, Style

# Inicializa a colorama
init(autoreset=True)

# Lista de mensagens para cada nível do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que retorna a cor correspondente ao nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED                 # Muito baixo
    elif nivel == 2:
        return Fore.YELLOW              # Baixo
    elif nivel == 3:
        return Fore.GREEN               # Médio
    elif nivel == 4:
        return Fore.CYAN                # Alto
    elif nivel == 5:
        return Fore.BLUE                # Muito alto
    else:
        return Fore.WHITE               # Caso nível inválido

# Simulação: testar níveis de 1 a 5
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(cor + mensagem + Style.RESET_ALL)