import sys
from usuarios import cadastrar_usuario, autenticar_usuario, logout, get_usuario_logado

# Variável global para controle do loop principal
EXECUTANDO = True


def menu_principal():
    """
    Exibe o menu principal para usuários NÃO autenticados.
    
    OPÇÕES:
        1. Login - Acessar o sistema
        2. Cadastrar Novo Usuário - Criar conta
        3. Sair - Encerrar aplicação
    
    RETORNO:
        str: Opção escolhida pelo usuário
    """
    print("\n--- TaskFlow - Gerenciador de Tarefas ---")
    print("1. Login")
    print("2. Cadastrar Novo Usuário")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    return escolha