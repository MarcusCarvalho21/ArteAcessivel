from bing_image_downloader import downloader
import os

'''
Dicas de palavras chave de pesquisa das obras
Nome Da Pintura + Nome do autor
Nome Da Pintura + "Exhibition"
Nome Da Pintura + "Original painting"
Nome Da Pintura + "Painting" + Nome do museu
'''

palavra_chave = "Adicona aqui o nome da pintura"
pasta_especifica = "Informe o caminho para salvar as imagens"

if not os.path.exists(pasta_especifica):
    os.makedirs(pasta_especifica)

downloader.download(palavra_chave, limit=80, output_dir=pasta_especifica, adult_filter_off=False, force_replace=False, timeout=60)
caminho_imagens = os.path.join(pasta_especifica, palavra_chave)

for i, filename in enumerate(os.listdir(caminho_imagens)):
    extensao = os.path.splitext(filename)[1] 
    novo_nome = f"{palavra_chave}_{i+1}{extensao}"
    caminho_antigo = os.path.join(caminho_imagens, filename)
    caminho_novo = os.path.join(pasta_especifica, novo_nome)
    os.rename(caminho_antigo, caminho_novo)

print(f"Download concluído! As imagens foram salvas e renomeadas na pasta: {pasta_especifica}")