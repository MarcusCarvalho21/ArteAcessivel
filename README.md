<h1 align="center">Arte Acessível</h1>
<hr>
<p align="justify">A detecção de objetos utilizando visão computacional tem se mostrado uma ferramenta muito poderosa em diversas áreas, incluindo a acessibilidade para pessoas com deficiência visual. Esse trabalho foca na comparação arquiteturas de redes neurais convolucionais(YOLOv8, YOLOv11, RetinaNet e Faster R-CNN) para detecção de obras pintadas, com o objetivo de avaliar sua viabilidade para aplicações de dispositivos móveis.  Os resultados demonstraram que os modelos YOLOv8 e YOLOv11 apresentaram  um desempenho superior em termo de precisão média (mAP) e recall, com um bom consumo de recursos durante o treinamento e tempo de inferência.</p>
<hr>
<h2 align="center">Documentação</h2>
<p>Para a iniciar o projeto, deve-se começar pela criação do dataset.</p>
<details close>
<summary>Criação do Dataset</summary>
<p>Para o perfeito funcionamento dos scripts de criação do dataset, é necessário a instalação correta das bibliotecas utilizadas.</p>

```bash
pip install -r requirements.txt
```
<p>Para realizar o download das imagens é necessário executar o script <strong>baixarImagens.py</strong>, seguindos as instruções contidas no arquivo.</p>

```bash
python baixarImagens.py
```

<p>Caso seja necessário, é possível renomear as imagens baixadas utilizando o script <strong>renomeiaImagem.py</strong>.</p>

```bash
python renomeiaImagem.py
```

<p>Para aplicar o augmentation nas imagens, basta utilizar o script <strong>adicionaAugmentations.py</strong>.</p>

```bash
python adicionaAugmentations.py
```
</details>
<details close>
<summary>Rotulagem de dados</summary>
<p>Após o download e organização das imagens, deve se realizar a rotulagem manual dos dados para em seguida partir para o treinamento dos modelos.
Existem diversos programas que possibilitam a rotulagem dos dados, o recomentado utilizar é o LabelImg, por sua facilidade de uso e execução na máquina local. Para utiliza-lo basta executar:</p>

```bash
labelImg DIRETÓRIO_IMAGEMS DETINO_ANOTAÇÕES CAMINHO_ARQUIVO_classes.txt
```
</details>
<details close>
<summary>Treinamento dos Modelos</summary>
<p>Após os dados rotulados, é possível executar o treinamento dos modelos. Como ambiente computacional, é possivel utilizar o Google Colab e Kaggle, sendo o segundo o mais recomendado por conta de seu tempo de uso ser maior.</p>

<p>Os códigos para treinamento está na parta <strong>ScriptsTreinamento</strong>.</p>
</details>