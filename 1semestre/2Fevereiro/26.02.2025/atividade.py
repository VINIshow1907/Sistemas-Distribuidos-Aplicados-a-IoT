valor = float(input("informe o valor do produto:"))
print("Forma de Pagamento")
print("1 - a vista \n -a prazo")
opcao = int(input("Escolha o pagamento (1 ou 2): "))
if opcao ==1:
    total = valor - (valor * 0.10)
    print("O total a pagar a vista =", total)
elif opcao ==2:
    print("O total a pagar a prazo =", valor)
else:
    print("Forma de pagamento inválida")

