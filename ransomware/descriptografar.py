from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    # Tenta descriptografar. Se o arquivo não estiver encriptado, o Fernet daria erro,
    # mas como filtramos antes, deve funcionar.
    dados_descriptografados = f.decrypt(dados)
    
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        if "venv" in raiz:
            continue
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # PROTEÇÃO IMPORTANTE:
            # Não tentar descriptografar o script de ataque, nem o de defesa, nem a chave
            if nome != "ransoware.py" and nome != "descriptografar.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista 

def main():
    chave = carregar_chave()
    # CORREÇÃO: Usar "." pois você já está na pasta
    arquivos = encontrar_arquivos(".")
    
    print(f"Arquivos para restaurar: {arquivos}")

    for arquivo in arquivos:
        try:
            descriptografar_arquivo(arquivo, chave)
            print(f"Sucesso: {arquivo}")
        except Exception as e:
            print(f"Erro ao descriptografar {arquivo}: {e}")

    print("Processo finalizado!")

if __name__ == "__main__":
    main()