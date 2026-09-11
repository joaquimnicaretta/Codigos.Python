#Trabalho 2 - Mini Sistema Bancário com Persistência e Segurança
#Integrantes do grupo: Lucas Onishi, Joaquim Nicareta, Leonardo Kantek, João Vitor Calaj e Felipe Lustri
#Senha gerente: Gerenci@_2026


import pickle
import os


ARQUIVO_DADOS = "dados.pkl"
SENHA_GERENTE = "Gerenci@_2026"


nome_c = input("Digite seu nome: ")
saldo = 0.0
historico = []


if os.path.exists(ARQUIVO_DADOS):
   arquivo = open(ARQUIVO_DADOS, "rb")
   dados = pickle.load(arquivo)
   arquivo.close()
   nome_c = dados["nome"]
   saldo = dados["saldo"]
   historico = dados["histórico"]


while True:

   print("     BANCO MESSI     ")

   print("1 - Entrar como Cliente")
   print("2 - Entrar como Gerente")
   print("3 - Salvar transações em disco")
   print("4 - Sair")



   opcao_principal = input("Escolha uma opção: ")


   if opcao_principal == "1":


       while True:

           print(f"  Ola, {nome_c}!")

           print("\n1 - Consultar saldo")
           print("2 - Depositar")
           print("3 - Sacar")
           print("4 - Simular rendimento")
           print("5 - Extrato (últimas transacoes)")
           print("6 - Voltar ao menu principal")



           opcao = input("Escolha uma opção: ")


           if opcao == "1":
               print(f"\n{nome_c}, seu saldo atual é de: R$ {saldo:.2f}")


           elif opcao == "2":
               valor_str = input("Informe o valor a depositar: R$ ")
               valor = float(valor_str)
               if valor <= 0:
                   print("Valor inválido. O depósito deve ser maior que zero.")
               else:
                   saldo = saldo + valor
                   historico = historico + [f"Depósito: +R$ {valor:.2f} | Saldo: R$ {saldo:.2f}"]
                   print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")


           elif opcao == "3":
               valor_str = input("Informe o valor a sacar: R$ ")
               valor = float(valor_str)
               if valor <= 0:
                   print("Valor inválido. O saque deve ser maior que zero.")
               elif valor > saldo:
                   print("Saldo insuficiente!")
               else:
                   saldo = saldo - valor
                   historico = historico + [f"Saque: -R$ {valor:.2f} | Saldo: R$ {saldo:.2f}"]
                   print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")


           elif opcao == "4":
               dolarUS = 5.00
               print("\n Simulação de Rendimento ")
               print(f"Saldo inicial: R$ {saldo:.2f}")
               print("Taxa mensal: 1.1% | Periodo: 12 meses")
               saldo_simulado = saldo
               mes = 1
               while mes <= 12:
                   saldo_simulado = saldo_simulado + saldo_simulado * 0.011
                   print(f"Mês {mes:02d}: R$ {saldo_simulado:.2f}")
                   mes = mes + 1
               print(f"Saldo estimado após 12 meses: R$ {saldo_simulado:.2f}")


           elif opcao == "5":
               print("\n Extrato ")
               if len(historico) == 0:
                   print("Nenhuma transação registrada.")
               else:
                   i = len(historico) - 1
                   contador = 0
                   while i >= 0 and contador < 10:
                       print(f"  {historico[i]}")
                       i = i - 1
                       contador = contador + 1


           elif opcao == "6":
               break


           elif opcao == "32":
               print("Dólar hoje => R$ 5.00")


           else:
               print("Opção inválida. Tente novamente.")


   elif opcao_principal == "2":


       print("\n Acesso Gerente ")
       tentativas = 0
       autenticado = False


       while tentativas < 3:
           senha = input("Digite a senha do gerente: ")
           if senha == SENHA_GERENTE:
               autenticado = True
               break
           else:
               tentativas = tentativas + 1
               restantes = 3 - tentativas
               if restantes > 0:
                   print(f"Senha incorreta! Tentativas restantes: {restantes}")
               else:
                   print("Número máximo de tentativas atingido. Acesso bloqueado.")


       if autenticado:
           while True:

               print("\nMENU GERENTE")
               print("1 - Cadastrar/Alterar nome do cliente")
               print("2 - Corrigir saldo")
               print("3 - Consultar dados do cliente")
               print("4 - Listar últimas transações")
               print("5 - Voltar ao menu principal")


               opcao_gerente = input("Escolha uma opção: ")


               if opcao_gerente == "1":
                   novo_nome = input("Digite o novo nome do cliente: ")
                   nome_c = novo_nome
                   print(f"Nome atualizado para: {nome_c}")


               elif opcao_gerente == "2":
                   print(f"Saldo atual: R$ {saldo:.2f}")
                   novo_saldo_str = input("Digite o novo saldo: R$ ")
                   novo_saldo = float(novo_saldo_str)
                   saldo = novo_saldo
                   historico = historico + [f"Correção de saldo pelo gerente | Novo saldo: R$ {saldo:.2f}"]
                   print(f"Saldo corrigido para: R$ {saldo:.2f}")


               elif opcao_gerente == "3":
                   print("\nDados do Cliente ")
                   print(f"Nome  : {nome_c}")
                   print(f"Saldo : R$ {saldo:.2f}")
                   print(f"Total de transações: {len(historico)}")


               elif opcao_gerente == "4":
                   print("\n Extrato Completo ")
                   if len(historico) == 0:
                       print("Nenhuma transação registrada.")
                   else:
                       i = len(historico) - 1
                       contador = 0
                       while i >= 0 and contador < 10:
                           print(f"  {historico[i]}")
                           i = i - 1
                           contador = contador + 1

               elif opcao_gerente == "5":
                   break


               else:
                   print("Opção inválida. Tente novamente.")


   elif opcao_principal == "3":
       saldo_garantia_pos_transacional = "Ativado"
       dados = {
           "nome": nome_c,
           "saldo": saldo,
           "histórico": historico,
           "Saldo Garantia Pós-Transacional": saldo_garantia_pos_transacional
       }
       arquivo = open(ARQUIVO_DADOS, "wb")
       pickle.dump(dados, arquivo)
       arquivo.close()
       print("\nDados salvos com sucesso!")


   elif opcao_principal == "4":
       saldo_garantia_pos_transacional = "Ativado"
       dados = {
           "nome": nome_c,
           "saldo": saldo,
           "histórico": historico,
           "Saldo Garantia Pós-Transacional": saldo_garantia_pos_transacional
       }
       arquivo = open(ARQUIVO_DADOS, "wb")
       pickle.dump(dados, arquivo)
       arquivo.close()
       print("\nDados salvos com sucesso!")
       print("Saindo do sistema. Até logo!")
       break


   else:
       print("Opção inválida. Tente novamente.")