#precisamos criar um programa que alimenta informações de livros, preço médio, quantidade de livros, mostra um resumo do que foi alimentado

from time import sleep

from Library.Functions import *
lislivro = []
lislivronova = []
lislivrovalor = []
numerocadastro = qtdcadastro()

for c in range(0,numerocadastro):
    nomecad = str(input(f"Digite o Nome do {c+1}° livro"))
    nomecad = nomecad.upper()
    valorcad = float(input(f"Digite o valor do livro"))
    lislivro.append(nomecad)
    lislivrovalor.append(valorcad)

sleep(3)
print("")

while True:

    print(""" Escolha uma das opções abaixo para os registros: \n
     1 - Procurar valor pelo nome do livro\n
     2 - Procurar livro pelo valor\n
     3 - Resumo dos dados\n
     4 - Registrar livros em arquivo\n
     0 - Sair""")

    try:
        esc = int(input("Digite o numero de sua escolha"))
        if esc ==1:
            nomeprocu = input("Digite o nome do livro procurado")
            nomeprocu = nomeprocu.upper()

            if nomeprocu in lislivro:
                valorprocu = lislivro.index(nomeprocu)
                print(f" o nome do livro é {nomeprocu}")
                print(f" e o valor do livro é {lislivrovalor[valorprocu]}")
            else:
                print("Livro não identificado :/, tente novamente")
                continue


        elif esc ==2:
            valorprocu = int(input("Digite o valor do livro procurado"))
            for c in range(0,len(lislivro)):
                if valorprocu in lislivrovalor:
                    indvalor = lislivrovalor.index(valorprocu)
                    print(f" o nome do livro é {lislivro[indvalor]}")
                else:
                    print("Valor não identificado :/, tente outro nome")
                    continue
        elif esc ==3:
            sleep(2)
            print(f"Resumo dos dados...")
            sleep(2)
            print(f'{"Livro":>10} {"Valor":>10}')
            for c in range(0, len(lislivro)):
                print(f'{lislivro[c]:>10} {lislivrovalor[c]:>10}')
        elif esc ==4:
            arq = str(input("Qual nome do arquivo que será gerado?"))
            arq = arq+".csv"
            arquivo = open(arq,'w')
            for c in range(0,len(lislivro)):
                arquivo.write(f"Livro: {lislivro[c]}, ")
                arquivo.write(f"Valor: {lislivrovalor[c]} ")
                arquivo.write("\n")
            arquivo.close()
        elif esc ==0:
            print("Obrigado por utilizar nosso app!!!")
            exit()
        else:
            print("Digite um valor válido, por favor")
            continue
    except (ValueError,TypeError):
        print("Digite um valor válido")
        continue

