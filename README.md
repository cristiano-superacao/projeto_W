# TaskFlow - Gerenciador de Tarefas

## Descricao

TaskFlow eh um sistema de gerenciamento de tarefas desenvolvido em Python que permite aos usuarios criar, editar, acompanhar e concluir tarefas com prazos definidos. O sistema foi projetado com foco em seguranca, boas praticas de programacao e facilidade de uso.

---

## Funcionalidades Principais

### Gerenciamento de Usuarios
- Cadastro de Novos Usuarios: Criar contas com nome, email, login e senha
- Autenticacao Segura: Login com hash SHA256 para protecao de senha
- Controle de Sessao: Gerenciamento de usuario logado
- Logout: Encerramento seguro de sessao

### Gerenciamento de Tarefas (CRUD)
- Criar Tarefas: Adicionar novas tarefas com titulo, descricao e prazo
- Listar Tarefas: Visualizar todas as tarefas pessoais
- Editar Tarefas: Modificar titulo, descricao ou prazo existentes
- Concluir Tarefas: Marcar tarefas como concluidas
- Excluir Tarefas: Remover tarefas do sistema
- Relatorios: Gerar relatorios sobre tarefas e prazos

### Estrutura de Dados de Tarefas
Cada tarefa contem:
- id: Identificador unico
- titulo: Nome da tarefa
- descricao: Descricao detalhada
- responsavel_id: ID do usuario responsavel
- responsavel_nome: Nome do responsavel
- prazo: Data limite (formato DD/MM/AAAA)
- status: Estado (Pendente, Concluida, Atrasada)
- criacao: Data e hora de criacao

---

## Estrutura de Arquivos

Task/
- main.py          # Interface principal (menus e fluxo do programa)
- usuarios.py      # Modulo de gerenciamento de usuarios
- Tarefas.py       # Modulo de gerenciamento de tarefas
- README.md        # Este arquivo
- utils/
  - arquivos.py  # Funcoes de leitura/escrita em JSON

---

## Principais Modulos

### main.py
Responsavel pela interface do usuario e fluxo principal da aplicacao.

Funcoes:
- menu_principal() - Menu inicial (Login, Cadastro, Sair)
- menu_logado() - Menu apos autenticacao
- tela_cadastro() - Interface de cadastro de usuarios
- tela_login() - Interface de login
- tela_criar_tarefa() - Interface para criar nova tarefa
- tela_editar_tarefa() - Interface para editar tarefa existente

---

### usuarios.py
Modulo de autenticacao e gerenciamento de usuarios com seguranca.

Funcoes Principais:
- cadastrar_usuario(nome, email, login, senha) - Registra novo usuario
- autenticar_usuario(login, senha) - Realiza login do usuario
- get_usuario_logado() - Retorna usuario em sessao
- logout() - Encerra sessao do usuario
- get_usuario_por_id(user_id) - Busca usuario por ID

Seguranca:
- Senhas armazenadas com hash SHA256 (unidirecional)
- Senhas nunca aparecem em texto puro
- Validacao de unicidade de login
- Sessao segura sem dados sensiveis

---

### Tarefas.py
Modulo de gerenciamento completo de tarefas (CRUD).

Funcoes Principais:
- criar_tarefa(titulo, descricao, prazo_str) - Cria nova tarefa
- listar_tarefas() - Exibe todas as tarefas do usuario
- editar_tarefa(tarefa_id, novo_titulo, nova_descricao, novo_prazo) - Modifica tarefa
- concluir_tarefa(tarefa_id) - Marca tarefa como concluida
- excluir_tarefa(tarefa_id) - Remove tarefa do sistema
- gerar_relatorio() - Relatorio de tarefas

Status de Tarefas:
- STATUS_PENDENTE: Aguardando execucao
- STATUS_CONCLUIDA: Tarefa finalizada
- STATUS_ATRASADA: Prazo vencido sem conclusao

---

## Como Usar

### 1. Executar o Programa
python main.py

### 2. Menu Principal
--- TaskFlow - Gerenciador de Tarefas ---
1. Login
2. Cadastrar Novo Usuario
3. Sair

### 3. Cadastrar Novo Usuario
- Escolha opcao 2 no menu inicial
- Forneca: nome completo, email, login e senha
- O sistema validara a unicidade do login

### 4. Fazer Login
- Escolha opcao 1 no menu inicial
- Informe login e senha
- O sistema autenticara suas credenciais

### 5. Gerenciar Tarefas
Apos login, voce tera acesso ao menu de tarefas:
--- Menu de [Seu Nome] ---
1. Minhas Tarefas
2. Criar Nova Tarefa
3. Editar Tarefa
4. Concluir Tarefa
5. Excluir Tarefa
6. Relatorios
7. Logout

#### Criar Tarefa
- Titulo: Resumo da tarefa
- Descricao: Detalhes sobre o que fazer
- Prazo: Data limite (formato DD/MM/AAAA)

#### Editar Tarefa
- Selecione o ID da tarefa a editar
- Deixe em branco os campos que nao quer alterar
- Atualize apenas o necessario

---

## Boas Praticas de Seguranca

1. Hash de Senhas: Utiliza SHA256 para criptografia unidirecional
2. Sessao Segura: Nunca armazena senhas em memoria
3. Validacao de Entrada: Verifica unicidade de login
4. Mensagens Genericas: "Login ou senha invalidos" (nao especifica o erro)
5. Isolamento de Dados: Usuarios so veem suas proprias tarefas

---

## Formato de Dados

### Usuarios (JSON)
{
  "id": 1,
  "nome": "Gabriela M Silva",
  "email": "gabriela.m.silva@ba.estudante.senai.br",
  "login": "gabriela_silva",
  "senha_hash": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
}

### Tarefas (JSON)
{
  "id": 1,
  "titulo": "Exemplo de Tarefa",
  "descricao": "Descricao detalhada",
  "responsavel_id": 1,
  "responsavel_nome": "Gabriela M Silva",
  "prazo": "31/12/2025",
  "status": "Pendente",
  "criacao": "2025-11-22 14:30:00"
}

---

## Exemplo de Fluxo Completo

1. Execute: python main.py
2. Escolha: 2 - Cadastrar Novo Usuario
3. Preencha os dados e confirme
4. Retorne ao menu e escolha: 1 - Login
5. Faca login com suas credenciais
6. Escolha: 2 - Criar Nova Tarefa
7. Preencha titulo, descricao e prazo
8. Veja suas tarefas com: 1 - Minhas Tarefas
9. Edite com: 3 - Editar Tarefa
10. Conclua com: 4 - Concluir Tarefa
11. Faca logout com: 7 - Logout

---

## Requisitos

- Python 3.7+
- Sistema de arquivos (para persistencia em JSON)
- Nenhuma dependencia externa

---

## Notas Importantes

- Persistencia: Dados sao salvos em arquivos JSON
- Validacao de Datas: Sempre use o formato DD/MM/AAAA
- Login Unico: Cada login deve ser unico no sistema
- Usuario Responsavel: Tarefas sao automaticamente atribuidas ao usuario logado

---

## Autor

Desenvolvido como um projeto educacional para demonstrar boas praticas em Python, incluindo:
- Modularizacao e separacao de responsabilidades
- Seguranca em autenticacao
- Persistencia de dados
- Interface interativa com usuario

---

## Licenca

Este projeto eh de codigo aberto e disponivel para fins educacionais.
