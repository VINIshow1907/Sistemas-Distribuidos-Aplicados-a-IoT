opcao = "s"
while (opcao == "s" or opcao == "S"):

    num1 = float(input("digite um número: "))
    num2 = float(input("digite outro número: "))
    soma = num1 + num2

    print(f"A soma de {num1:.1f} + {num2:.1f} = {soma:.1f}\\n")
    opcao= input("Deseja continuar o cálculo da soma de outros números?\\n"
                 "Tecle [S] para continuar ou [N] para terminar: ")
    print("\\n")