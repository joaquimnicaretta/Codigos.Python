import math
import random

PERFIS = {
    'P1': ('Uso Leve',     'navegação básica e acessos pontuais',      (60,150),  (3,15),  (1,3),  (100,300)),
    'P2': ('Uso Moderado', 'streaming e videoconferências',             (140,260), (12,30), (3,5),  (280,480)),
    'P3': ('Uso Intenso',  'gamer ou grande movimentação de arquivos',  (240,400), (28,60), (5,10), (450,700)),
}


def exibir_perfis():
    print(" PERFIS DE CLASSIFICAÇÃO ")
    for codigo, (nome, detalhe, *_) in PERFIS.items():
        print(f"  {codigo} — {nome}: {detalhe}")

def criar_banco():
    banco = []
    print("\n Criação do banco de dados ")
    qtd = int(input("  Quantos registros no banco? "))
    for _ in range(qtd):
        banco.append([
            random.randint(60,  400),
            random.randint(3,   60),
            random.randint(1,   10),
            random.randint(100, 700),
        ])
    return banco

def classificar_registro(registro):
    for codigo, (_, _, dl, ul, ac, tp) in PERFIS.items():
        download_ok = dl[0] <= registro[0] <= dl[1]
        upload_ok   = ul[0] <= registro[1] <= ul[1]
        acessos_ok  = ac[0] <= registro[2] <= ac[1]
        tempo_ok    = tp[0] <= registro[3] <= tp[1]

        if download_ok and upload_ok and acessos_ok and tempo_ok:
            return codigo

    return 'P2'  # se nao se encaixar em nenhum, assume moderado


def classificar_banco(banco):
    banco_classificado = []
    for registro in banco:
        perfil = classificar_registro(registro)
        banco_classificado.append(registro + [perfil])
    return banco_classificado

def exibir_banco(banco):
    print("\n" + "=" * 65)
    print(" BANCO DE DADOS ".center(65))
    print("=" * 65)
    print(f"  {'#':<4} {'Download':>10} {'Upload':>8} {'Acessos':>9} {'Tempo':>7} {'Perfil':>8}")
    print("-" * 65)
    for i, registro in enumerate(banco):
        print(f"  {i+1:<4} {registro[0]:>8}MB {registro[1]:>6}MB {registro[2]:>9} {registro[3]:>6}min {registro[4]:>8}")
    print("=" * 65)

def calc_dist(usuario, registro):
    return math.sqrt(sum((usuario[i] - registro[i]) ** 2 for i in range(4)))

def classificar_usuario(usuario, banco):
    menor = None
    perfil = None
    for registro in banco:
        d = calc_dist(usuario, registro)
        if menor is None or d < menor:
            menor = d
            perfil = registro[4]
    return perfil, menor

exibir_perfis()

banco_bruto      = criar_banco()
banco            = classificar_banco(banco_bruto)
exibir_banco(banco)

while True:
    print("\n--- Classificação ---")
    quantidade = int(input("  Quantos usuários gerar? (0 para sair) "))
    if quantidade == 0:
        print("  Encerrando. Até logo!")
        break

    for i in range(quantidade):
        usuario = [
            random.randint(60, 400),
            random.randint(3, 60),
            random.randint(1, 10),
            random.randint(100, 700),
        ]
        perfil, distancia = classificar_usuario(usuario, banco)
        nome, detalhe, *_ = PERFIS[perfil]

        print(f"\n  Usuário {i+1}:")
        print(f"    Dados    : download={usuario[0]}MB | upload={usuario[1]}MB | acessos={usuario[2]} | tempo={usuario[3]}min")
        print(f"    Distância: {distancia:.2f}")
        print(f"    Resultado: {perfil} — {nome}: {detalhe}")