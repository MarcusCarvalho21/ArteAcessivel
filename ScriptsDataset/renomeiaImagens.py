import os

def renomear_arquivos(pasta, novo_nome):
    """
    Renomeia as imagens e salva no caminho especificado.
    
    Args:
        pasta (str): Diretório em que está salva as imagens.
        novo_nome (str): Novo nome para os arquivos.
    """

    arquivos = os.listdir(pasta)
    arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(pasta, arquivo))]

    for indice, arquivo in enumerate(arquivos, start=1):      
        extensao = os.path.splitext(arquivo)[1]
        novo_nome_arquivo = f"{novo_nome}_{indice}{extensao}"
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome_arquivo)
        os.rename(caminho_antigo, caminho_novo)
    print(f"Todos os arquivos foram renomeados para '{novo_nome}_X'")

pasta = 'Adicione o caminho para as imagens'
novo_nome = 'Novo nome das imagens'
renomear_arquivos(pasta, novo_nome)