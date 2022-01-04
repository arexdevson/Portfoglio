import time
from PIL import Image,ImageFont,ImageDraw
from datetime import date

inicio = time.time()

with open("nomes.txt",'r') as nome:
    #com isso eu pego todos os nomes que tenho no meu arquivo, porém eles estão juntos e assim que rodo um print
    # o python identifica um \n separando cada palavra, que no código significa espaço, portanto, podemos separar cada nome os incluindo em uma lista realizando um split
    nomes = nome.read()
    #para cada nome na minha lista de nomes, faça a separação deles considerando caractere \n
    for nome in nomes.split('\n'):


        #coordenadas - #primeiro a distância da esquerda pra direita e o segundo altura (de cima pra baixo)
        coord_pessoa = 339,420
        coord_diretor = 225,630
        coord_data = 640,630

        #dados pra preenchimento
        nome_pessoa = nome
        nome_diretor = "Alex Sandro Da S X Argemi"
        data_hoje = date.today().strftime('%d/%m/%Y')

        #abrindo imagem
        imagem = Image.open(r'certified.png')

        #fonte usada
        caminho_fonte = r"C:\Windows\Fonts\Ebrima.ttf"
        font = ImageFont.truetype(caminho_fonte,24)

        #cor
        rgb_preto = (0,0,0)

        #começar a desenhar na imagem
        desenho = ImageDraw.Draw(imagem)
        desenho.text(coord_pessoa,nome_pessoa,font=font,fill=rgb_preto)
        desenho.text(coord_diretor,nome_diretor,font=font,fill=rgb_preto)
        desenho.text(coord_data,data_hoje,font=font,fill=rgb_preto)
        imagem.save(f'{nome_pessoa}.png')

fim = time.time()

#quanto tempo nossa aplicação rodou?

print(f" Finalizado em {fim-inicio:2f} segundos")