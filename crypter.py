from cryptography.fernet import Fernet
import os

# Geração de chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    return chave

# Carregar chave
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

# Criptografar arquivos
def criptografar_arquivos(diretorio):
    chave = carregar_chave()
    fernet = Fernet(chave)
    
    for filename in os.listdir(diretorio):
        caminho = os.path.join(diretorio, filename)
        if os.path.isfile(caminho):
            with open(caminho, "rb") as file:
                dados = file.read()
            dados_encriptados = fernet.encrypt(dados)
            with open(caminho, "wb") as file:
                file.write(dados_encriptados)
            print(f"{filename} criptografado com sucesso!")

# Descriptografar arquivos
def descriptografar_arquivos(diretorio):
    chave = carregar_chave()
    fernet = Fernet(chave)
    
    for filename in os.listdir(diretorio):
        caminho = os.path.join(diretorio, filename)
        if os.path.isfile(caminho):
            with open(caminho, "rb") as file:
                dados = file.read()
            dados_decriptados = fernet.decrypt(dados)
            with open(caminho, "wb") as file:
                file.write(dados_decriptados)
            print(f"{filename} descriptografado com sucesso!")

# Menu principal
if __name__ == "__main__":
    print("Simulação de Criptografia de Arquivos")
    print("1. Gerar chave")
    print("2. Criptografar arquivos")
    print("3. Descriptografar arquivos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        gerar_chave()
        print("Chave gerada e salva como 'chave.key'.")
    elif opcao == "2":
        diretorio = input("Informe o diretório onde estão os arquivos: ")
        criptografar_arquivos(diretorio)
    elif opcao == "3":
        diretorio = input("Informe o diretório onde estão os arquivos: ")
        descriptografar_arquivos(diretorio)
    elif opcao == "4":
        print("Saindo...")
    else:
        print("Opção inválida.")
