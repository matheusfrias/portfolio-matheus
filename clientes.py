import json
import os

ARQUIVO = "clientes.json"

def inicializar():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w") as f:
            json.dump([], f)

def carregar():
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar(clientes):
    with open(ARQUIVO, "w") as f:
        json.dump(clientes, f, indent=4)

def validar_email(email):
    return "@" in email and "." in email

def cadastrar():
    print("\n=== CADASTRAR CLIENTE ===")
    nome = input("Nome: ").strip()
    
    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            break
        print("❌ Email inválido")

    telefone = input("Telefone: ").strip()

    clientes = carregar()
    clientes.append({
        "nome": nome,
        "email": email,
        "telefone": telefone
    })

    salvar(clientes)
    print("✅ Cliente cadastrado!\n")

def listar():
    clientes = carregar()

    if not clientes:
        print("⚠️ Nenhum cliente cadastrado.\n")
        return

    print("\n=== LISTA DE CLIENTES ===")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c['nome']} | {c['email']} | {c['telefone']}")
    print()

def buscar():
    termo = input("Buscar nome: ").lower()
    clientes = carregar()

    resultados = [c for c in clientes if termo in c["nome"].lower()]

    if resultados:
        for c in resultados:
            print(f"{c['nome']} | {c['email']} | {c['telefone']}")
    else:
        print("❌ Nenhum encontrado")
    print()

def editar():
    listar()
    clientes = carregar()

    try:
        indice = int(input("Número do cliente: ")) - 1
        cliente = clientes[indice]

        print(f"Editando: {cliente['nome']}")
        cliente["nome"] = input("Novo nome: ") or cliente["nome"]
        cliente["email"] = input("Novo email: ") or cliente["email"]
        cliente["telefone"] = input("Novo telefone: ") or cliente["telefone"]

        salvar(clientes)
        print("✅ Atualizado!\n")
    except:
        print("❌ Erro ao editar\n")

def excluir():
    listar()
    clientes = carregar()

    try:
        indice = int(input("Número do cliente para excluir: ")) - 1
        removido = clientes.pop(indice)

        salvar(clientes)
        print(f"🗑️ Removido: {removido['nome']}\n")
    except:
        print("❌ Erro ao excluir\n")

def menu():
    inicializar()

    while True:
        print("=== SISTEMA DE CLIENTES ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Editar")
        print("5 - Excluir")
        print("6 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            editar()
        elif opcao == "5":
            excluir()
        elif opcao == "6":
            break
        else:
            print("❌ Opção inválida\n")

menu()