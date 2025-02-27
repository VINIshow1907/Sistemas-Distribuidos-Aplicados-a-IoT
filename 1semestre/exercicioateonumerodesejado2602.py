opcao = "s"
while (opcao == "s" or opcao == "S"):
    num1 = float(input("digite o número inicial da contagem: "))
    num2 = float(input("digite o número final da contagem: "))
    while (num1 < num2 or num1 > num2):
        if (num1 < num2):
            num1 = num1 + 1
            print(f"{num1:.1f}")
        else:
            num1 = num1 - 1
            print(f"{num1:.1f}")
    opcao= input("Deseja continuar?\n"
                 "Tecle [S] para continuar ou [N] para terminar: ")
    print("\n")