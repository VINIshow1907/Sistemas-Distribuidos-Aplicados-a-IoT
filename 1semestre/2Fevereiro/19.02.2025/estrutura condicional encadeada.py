n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))          
n4 = float(input("Digite a nota 4: "))
media = (n1 + n2 + n3 + n4) / 4
if (media >= 6):
    print(f"Sua média foi {media:.2f} e você está aprovado")
elif (media < 6 and media >= 3):
    print(f"Sua média foi {media:.2f} e você está de recuperação")
else:
    print(f"Sua média foi {media:.2f} e você está reprovado")