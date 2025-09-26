# API de Dados do Google Sheets

Este projeto cria uma **API em Python (Flask)** que consome dados de uma planilha do **Google Sheets**, valida os dados e os disponibiliza via uma rota HTTP. A API está hospedada no **Render**, e os dados podem ser acessados diretamente pelo site (https://heitorab06.github.io/Processo-Seletivo-Rede-Alpha-Fitness/).

---

## 📝 Funcionalidades

- Lê dados de uma planilha do Google Sheets via link CSV.
- Remove linhas com dados inválidos ou nulos.
- Valida campos importantes:
  - **Email**: garante formato válido (letras, números e pontos antes do `@`).
  - **CPF**: verifica se está no formato correto.
  - **Número de telefone**: validação de dígitos.
- Barra de pesquisa interativa
- Disponibiliza os dados filtrados via **rota `/dados`** em formato JSON.
- Fácil de consumir em frontend ou outras aplicações.

---

## 🚀 Tecnologias

- **Python 3**
- **Flask**: framework web
- **pandas**: manipulação de dados
- **flask-cors**: habilita requisições cross-origin
- **Render**: hospedagem gratuita da API

---
