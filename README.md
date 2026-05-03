🏞️ Controle de Níveis de Água – Terminal com Colorama

Este projeto simula um sistema simples de monitoramento de níveis de água em um reservatório.
Ele exibe mensagens coloridas no terminal utilizando a biblioteca colorama, seguindo diferentes níveis de risco.

📌 Objetivo do Sistema

O programa apresenta mensagens de alerta conforme o nível do reservatório, ajudando a visualizar de forma clara o status atual da água.

Cada nível possui:

Uma mensagem específica
Uma cor correspondente
Uma progressão de risco (de crítico a alerta máximo)
🚨 Níveis do Reservatório
Nível	Situação	Cor usada
1	Muito baixo (crítico)	Vermelho
2	Baixo	Amarelo
3	Médio	Verde
4	Alto	Ciano
5	Muito alto (alerta)	Azul
🧠 Tecnologias e Conceitos Utilizados
Python 3
colorama (para colorir mensagens no terminal)
Listas
Funções
Estrutura sequencial
Simulação de níveis (sem entrada de usuário)
🧩 Como funciona o código

O programa:

Importa a biblioteca colorama
Define uma lista com os 5 níveis de alerta
Usa uma função para determinar a cor de cada nível
Exibe no terminal cada nível com sua cor correspondente
Restaura o estilo padrão automaticamente
🧪 Exemplo de Execução

Ao rodar o código, você verá no terminal algo como:

Nível 1 - Muito baixo (crítico)   → vermelho  
Nível 2 - Baixo                   → amarelo  
Nível 3 - Médio                   → verde  
Nível 4 - Alto                    → ciano  
Nível 5 - Muito alto (alerta)     → azul