from datetime import datetime
from usuarios import get_usuario_logado

# Constantes para Status da Tarefa (evita erros de digitação)
STATUS_PENDENTE = "Pendente"
STATUS_CONCLUIDA = "Concluída"
STATUS_ATRASADA = "Atrasada"


def _carregar_tarefas():
    return ler_dados(ARQUIVO_TAREFAS)

def _salvar_tarefas(tarefas):
    return salvar_dados(ARQUIVO_TAREFAS, tarefas)


def criar_tarefa(titulo, descricao, prazo_str):
    usuario = get_usuario_logado()
    if not usuario:
        print("Erro: Nenhum usuário logado para criar a tarefa.")
        return False

    try:
        # Validação básica do formato da data
        prazo = datetime.strptime(prazo_str, '%d/%m/%Y').strftime('%d/%m/%Y')
    except ValueError:
        print("Erro: Formato de prazo inválido. Use DD/MM/AAAA.")
        return False