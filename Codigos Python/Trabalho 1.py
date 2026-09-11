import random
energia=100

print("Você acorda em uma ilha deserta após um naufrágio. O sol quente bate em sua pele, e o som das ondas quebra o silêncio. Sua última lembrança é do barco afundando durante uma tempestade. Agora, você precisa tomar decisões para garantir sua sobrevivência.")
print(f"Energia atual {energia}")
#CENARIO 1
print("Cenário 1")
print("1 - Explorar a floresta")
print("2 - Caminhar pela praia")

escolha1 = int(input("Escolha seu caminho (1 ou 2):"))

if escolha1 == 1:
    perda = random.randint(20,40)
    energia -= perda
    print("Você entrou na floresta")
    print(f"Você perdeu {perda} de energia. Sua energia atual é de {energia}")
elif escolha1 == 2:
    perda = random.randint(20, 40)
    energia -= perda
    print("Você caminhou pela praia")
    print(f"Você perdeu {perda} de energia. Sua energia atual é de {energia}")

#cenarios 2
if escolha1 == 1:
    print("Você entra na floresta e logo encontra um pequeno rio de água cristalina. A sombra das árvores oferece um alívio do calor intenso")
    print("Você está com sede. Você pode escolher beber do rio à sua frente ou buscar outra fonte de água")
    print("1 - Beber a água do rio à sua frente")
    print("2 - Procurar outra fonte de água")
    escolha2 = int(input("Escolha onde beber água (1 ou 2):"))
    if escolha2 == 1:
        perda = random.randint(15,35)
        energia -= perda
        print("Você escolheu beber água do rio, mas começou a passar mal. O que deseja fazer?")
        print(f"Seu estado atual de energia é de {energia}")

        print("1 - Beber mais água do rio")
        print("2 - Procurar uma fonte de água mais segura")

        escolha_ex1 = int(input("Escolha:"))

        if escolha_ex1 == 1:
            perda = random.randint(15,35)
            energia -= perda
            print("Você piorou!")
            print(f"Perdeu {perda} de energia")
            print(f"Seu estado atual de energia é de {energia}")
        elif escolha_ex1 == 2:
            ganho = random.randint(5, 15)
            energia += ganho
            print("Você escolheu procurar por outra fonte de água")
            print("Você, andando pela floresta, encontrou um coqueiro e conseguiu beber água de coco")

            print(f"Você tomou a água de coco e ganhou {ganho} de energia")
            print(f"Você está com {energia} de energia atualmente")
    if escolha2 == 2:
        ganho = random.randint(5, 15)
        energia += ganho
        print("Você escolheu procurar por outra fonte de água")
        print("Você, andando pela floresta, encontrou um coqueiro e conseguiu beber água de coco")

        print(f"Você tomou a água de coco e ganhou {ganho} de energia")
        print(f"Você está com {energia} de energia atualmente")


elif escolha1 == 2:
    print("Você, andando pela praia, começa a sentir calor e fome")
    print("1 - Caçar ou pescar")
    print("2 - Procurar frutas")

    escolha2 = int(input("Escolha (1 ou 2):"))
    if escolha2 == 1:
        perda = random.randint(15,35)
        energia -= perda
        print("Você não conseguiu encontrar comida")
        print(f"Perdeu {perda} de energia e sua energia atual é de {energia}")
    elif escolha2 == 2:
        ganho = random.randint(10,25)
        energia += ganho
        print("Você encontrou frutas e se sente com mais energia")
        print(f"Você ganhou {ganho} de energia")

#CENARIO 3
print("O sol começa a se pôr, e a temperatura cai rapidamente. O vento aumenta, e você sabe que precisa se preparar para a noite")
print("Você encontrou destroços de seu barco. Nos destroços há madeiras, cordas e pedaços de tecido")
print("O que gostaria de fazer com eles?")
print("1 - Construir um abrigo")
print("2 - Acender uma fogueira")

escolha3 = int(input("Escolha (1 ou 2):"))
if escolha3 == 1:
    perda = random.randint(15,35)
    energia -= perda
    print("Você construiu um abrigo")
    print(f"Perdeu {perda} de energia e sua energia atual é de {energia}")
elif escolha3 == 2:
    perda = random.randint(5,15)
    energia -= perda
    print("Você acendeu uma fogueira")
    print(f"Perdeu {perda} de energia e sua energia atual é de {energia}")

#Final

print("Você foi resgatado da ilha")

if energia > 70:
    print(f"FINAL ALEGRE - Você terminou com {energia} de energia e está ótimo, parecendo que estava em um resort e não em uma ilha")
elif energia >=30 and energia <=69:
    print(f"FINAL IRÔNICO - Você terminou com {energia} de energia e está tão fraco que não consegue nem fazer piadas. Além de estar parecendo um zumbi")
else:
    print(f"FINAL SURREAL - Você terminou com {energia} de energia e está quase sem forças e vai precisar de suporte para voltar a como vivia antes")