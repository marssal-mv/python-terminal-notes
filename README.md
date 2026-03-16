# 📝 App de Anotações (Terminal CRUD)

Meu primeiro projeto em Python criado para o GitHub! Este é um aplicativo de terminal simples e eficiente que funciona como um sistema CRUD (Create, Read, Update, Delete) completo para gerenciar anotações de texto.

## 🚀 Funcionalidades

- **Criar (Create):** Adicione novas notas facilmente.
- **Listar (Read):** Visualize todas as suas anotações salvas.
- **Atualizar (Update):** Edite o texto de notas já existentes através do seu ID.
- **Deletar (Delete):** Remova anotações que não são mais necessárias.
- **Persistência de Dados:** Suas notas são salvas automaticamente em um arquivo `notas.json`. Você pode fechar o programa e, ao abrir novamente, as suas anotações continuarão lá!

## 🛠️ Tecnologias Utilizadas

- **Python 3:** Linguagem base do projeto.
- **JSON (Módulo Nativo):** Para manipulação e persistência dos dados.
- **OS (Módulo Nativo):** Para manipulação segura de caminhos de arquivos e verificações no sistema operacional.

## 🧠 Aprendizados e Destaques do Código

Este projeto foi construído para praticar e demonstrar conceitos importantes de programação e Python:

- **Controle de Fluxo:** Utilização de blocos `while True` e estruturas condicionais para gerenciar o menu principal.
- **Manipulação de Arquivos e Formato JSON:** Salvando estruturas de dicionários/listas utilizando a função embutida `json.dump` e recuperando com `json.load`.
- **Tratamento de Exceções (Robustez):** Uso de `try/except` para prevenir o "crash" do programa em caso de entradas inválidas do usuário ou caso ocorram erros de formatação (como a exceção `json.JSONDecodeError`).
- **Boas Práticas de Código:** 
  - Estruturação usando funções curtas e reaproveitáveis (como `carregar_notas` e `salvar_notas`).
  - Utilização da estrutura `if __name__ == "__main__":` para proteger a execução importada do script.
  - O código salva corretamente caracteres especiais e acentuações (`ensure_ascii=False` e codificação UTF-8).

## 💻 Como Rodar na Sua Máquina

### Pré-requisitos
- É preciso ter o [Python](https://www.python.org/downloads/) instalado no seu computador.

### Passo a Passo

1. Realize o clone deste repositório:
   ```bash
   git clone seu-link-do-repositorio-aqui
   ```

2. Abra o terminal e navegue até a pasta do projeto:
   ```bash
   cd nome-da-pasta-do-projeto
   ```

3. Execute o script principal:
   ```bash
   python app.py
   ```
   
4. O menu interativo aparecerá. Siga os números sugeridos para começar a utilizar!

---
*Projeto desenvolvido sob mentoria de Python. Sinta-se à vontade para enviar dicas ou Pull Requests!*
