"""
================================================================================
MÓDULO: relatorios.py
================================================================================
DESCRIÇÃO:
    Módulo responsável pela GERAÇÃO E EXPORTAÇÃO DE RELATÓRIOS.
    Fornece análises e visualizações das tarefas do sistema através
    de filtros específicos.

FUNCIONALIDADES PRINCIPAIS:
    - Filtrar tarefas por status (Concluídas, Pendentes, Atrasadas)
    - Exibir relatórios formatados no console
    - Exportar relatórios para arquivos TXT
    - Cálculo automático de tarefas atrasadas

TIPOS DE RELATÓRIOS:
    1. Tarefas Concluídas: Todas as tarefas finalizadas
    2. Tarefas Pendentes: Tarefas ainda não concluídas
    3. Tarefas Atrasadas: Tarefas pendentes com prazo vencido

FORMATO DE EXPORTAÇÃO:
    - Arquivos TXT com encoding UTF-8
    - Nome com timestamp (evita sobrescrever)
    - Inclui todos os detalhes da tarefa
    - Informações do responsável

IMPORTANTE PARA APRESENTAÇÃO:
    Este módulo demonstra análise de dados e geração de relatórios,
    funcionalidades essenciais para tomada de decisões gerenciais.
================================================================================
"""
