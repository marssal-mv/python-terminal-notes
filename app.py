import json
import os

ARQUIVO_NOTAS = "notas.json"

def carregar_notas():
    """
    Carrega as notas do arquivo JSON.
    Se o arquivo não existir ou estiver vazio, retorna uma lista vazia.
    """
    if not os.path.exists(ARQUIVO_NOTAS):
        return []
    try:
        with open(ARQUIVO_NOTAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_notas(notas):
    """Salva a lista atual de notas no arquivo JSON."""
    with open(ARQUIVO_NOTAS, 'w', encoding='utf-8') as f:
        # ensure_ascii=False permite salvar caracteres especiais como acentos corretamente
        json.dump(notas, f, ensure_ascii=False, indent=4)

def criar_nota(notas):
    """Solicita texto ao usuário, cria uma nova nota na lista e salva no arquivo."""
    texto = input("Digite o texto da sua nova nota: ")
    
    # Gera um ID incrementando o maior ID existente, ou 1 se for a primeira nota
    novo_id = 1 if not notas else max(nota.get("id", 0) for nota in notas) + 1
    
    nova_nota = {"id": novo_id, "texto": texto}
    notas.append(nova_nota)
    salvar_notas(notas)
    
    print(f"\n✅ Nota {novo_id} criada com sucesso!")

def listar_notas(notas):
    """Exibe todas as notas armazenadas na tela."""
    print("\n--- Suas Notas ---")
    if not notas:
        print("Nenhuma nota encontrada. Crie uma nova!")
    else:
        for nota in notas:
            print(f"[{nota['id']}] {nota['texto']}")
    print("------------------")

def atualizar_nota(notas):
    """Permite ao usuário editar o texto de uma nota existente a partir de seu ID."""
    listar_notas(notas)
    if not notas:
        return

    try:
        nota_id = int(input("Digite o ID da nota que deseja atualizar: "))
    except ValueError:
        print("\n❌ ID inválido. Digite apenas números.")
        return

    # Busca a nota pelo ID fornecido
    for nota in notas:
        if nota["id"] == nota_id:
            print(f"\nTexto atual: {nota['texto']}")
            novo_texto = input("Novo texto: ")
            nota["texto"] = novo_texto
            salvar_notas(notas)
            print(f"\n✅ Nota {nota_id} atualizada com sucesso!")
            return
    
    print(f"\n❌ Nota com ID {nota_id} não encontrada.")

def deletar_nota(notas):
    """Remove uma nota da lista com base no ID fornecido."""
    listar_notas(notas)
    if not notas:
        return

    try:
        nota_id = int(input("Digite o ID da nota que deseja deletar: "))
    except ValueError:
        print("\n❌ ID inválido. Digite apenas números.")
        return

    # Procura e remove a nota correspondente
    for i, nota in enumerate(notas):
        if nota["id"] == nota_id:
            del notas[i]
            salvar_notas(notas)
            print(f"\n✅ Nota {nota_id} deletada com sucesso!")
            return
    
    print(f"\n❌ Nota com ID {nota_id} não encontrada.")

def menu():
    """Exibe as opções do app e retorna a escolha do usuário."""
    print("\n=== App de Anotações ===")
    print("1. Criar nota")
    print("2. Listar notas")
    print("3. Atualizar nota")
    print("4. Deletar nota")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")

def main():
    """Fluxo principal do aplicativo (Main Loop)."""
    # 1. Carrega os dados iniciais do arquivo JSON
    notas = carregar_notas()
    
    # 2. Inicia o loop infinito do programa
    while True:
        opcao = menu()
        
        # 3. Chama a função apropriada com base na escolha
        if opcao == '1':
            criar_nota(notas)
        elif opcao == '2':
            listar_notas(notas)
        elif opcao == '3':
            atualizar_nota(notas)
        elif opcao == '4':
            deletar_nota(notas)
        elif opcao == '5':
            print("\nSaindo do programa. Até mais! 👋")
            break
        else:
            print("\n❌ Opção inválida! Escolha um número de 1 a 5.")

# Garantia de que main() só roda se o script for executado diretamente
if __name__ == "__main__":
    main()
